# Day 15 – AI Evaluation, Hallucinations and Guardrails: Submission Report

**Name:** ____________
**Repository link:** ____________

## 1. Objective
Test how an LLM behaves on supported and unsupported questions, and add guardrails so it does not answer confidently when information is missing.

## 2. Hallucination experiment (no context)
Paste from `hallucination_experiment.md`:
- Question: "What is the annual revenue of NovaTech Solutions?"
- AI answer: ____________
- Observation: ____________ (did it guess or admit it doesn't know?)

## 3. Knowledge base (8 facts)
See `knowledge_base.json`.

## 4. Evaluation dataset (10 questions)
See `test_questions.json`: 5 supported, 1 partial, 4 outside the knowledge base.

## 5. Results
Paste the tables from `results.md` here (Question | Expected | AI Answer | Correct?) for all three versions.

| Version | Score |
|---|---|
| 1. Before (weak prompt) | _/10 |
| 2. Guarded prompt | _/10 |
| 3. Guarded prompt + output guardrail | _/10 |

## 6. Key before/after example
- **Question:** Does TaskFlow integrate with Jira?
- **Before:** ____________ (unreliable answer)
- **After:** "I don't have enough information to answer that."
- **Why it changed:** The prompt limits the model to the knowledge base, and the code guardrail replaces any answer to an out-of-scope question with a safe refusal.

## 7. Guardrails implemented
1. Prompt-based: answer only from the provided information, else refuse.
2. Output check in code (`output_guardrail` in `assistant.py`).

## 8. Failures and learnings
- ____________ (questions that still failed and why)
- Evaluation datasets allow repeatable testing after any prompt, model or retrieval change.
- Reliable AI systems need testing and controlled behaviour, not just a good prompt.
