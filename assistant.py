"""NovaTech support assistant with prompt + output guardrails (Day 15)."""
import os
import json
import time
import requests

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL = os.environ.get("MODEL", "gemini-2.0-flash")
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

REFUSAL = "I don't have enough information to answer that."

with open(os.path.join(os.path.dirname(__file__), "knowledge_base.json"), encoding="utf-8") as f:
    KB = json.load(f)
CONTEXT = "\n".join(f"- {fact}" for fact in KB)

# Version 1: no restrictions (used to show hallucination / unreliable behaviour)
BASELINE_PROMPT = "You are a helpful assistant for NovaTech Solutions. Answer the user's question."

# Version 2: prompt-based guardrail
GUARDED_PROMPT = (
    "You are a support assistant for NovaTech Solutions.\n"
    "Answer ONLY using the information below. Do not use outside knowledge.\n"
    f"If the answer is not in the information, reply exactly: \"{REFUSAL}\"\n"
    "If only part of the question can be answered, answer that part and clearly say "
    "you don't have information for the rest.\n\n"
    "INFORMATION:\n" + CONTEXT
)


def ask_llm(system_prompt: str, question: str) -> str:
    """Send one question to Gemini and return the text answer."""
    if not API_KEY:
        raise SystemExit("GEMINI_API_KEY is not set. See README.md.")
    body = {
        "system_instruction": {"parts": [{"text": system_prompt}]},
        "contents": [{"role": "user", "parts": [{"text": question}]}],
        "generationConfig": {"temperature": 0},
    }
    last_error = "unknown error"
    for attempt in range(4):
        try:
            r = requests.post(URL, params={"key": API_KEY}, json=body, timeout=(15, 120))
        except requests.exceptions.RequestException as e:
            # timeout / connection problem: wait and retry instead of crashing
            last_error = f"network error: {type(e).__name__}"
            time.sleep(5 * (attempt + 1))
            continue
        if r.status_code == 200:
            try:
                return r.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
            except (KeyError, IndexError):
                return "ERROR: empty response"
        last_error = f"ERROR {r.status_code}: {r.text[:150]}"
        if r.status_code in (400, 401, 403, 404):
            break  # retrying will not help (bad key / model / request)
        time.sleep(5 * (attempt + 1))
    return last_error


def is_refusal(answer: str) -> bool:
    a = answer.lower()
    return "don't have enough information" in a or "do not have enough information" in a


def output_guardrail(answer: str, in_scope: bool):
    """Code-level guardrail.
    If the question is outside the knowledge base but the model still tried to
    answer, replace the answer with the safe refusal.
    Returns (final_answer, guardrail_triggered)."""
    if not in_scope and not is_refusal(answer):
        return REFUSAL, True
    return answer, False


def answer_question(question: str, in_scope: bool = True) -> str:
    """Production-style call: guarded prompt + output guardrail."""
    raw = ask_llm(GUARDED_PROMPT, question)
    final, _ = output_guardrail(raw, in_scope)
    return final


if __name__ == "__main__":
    print("NovaTech assistant (type 'quit' to exit)")
    while True:
        q = input("\nYou: ").strip()
        if q.lower() in {"quit", "exit"}:
            break
        print("Bot:", ask_llm(GUARDED_PROMPT, q))
