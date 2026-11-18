# Evaluation Results

## 1. BEFORE (weak prompt): 3/10 correct

| Question | Type | Expected | AI Answer | Result |
|---|---|---|---|---|
| Who founded NovaTech Solutions? | supported | Ayesha Khan | NovaTech Solutions was founded by Sarah Jenkins and Marcus Vance in 2012. | FAIL |
| How much does the TaskFlow Pro plan cost? | supported | $25 per user per month | The TaskFlow Pro plan costs **$49 per user, per month** (billed annually) or **$59 per user, per month** (billed monthly).   If you have any other questions abo | FAIL |
| Which tools does TaskFlow integrate with? | supported | Slack, Google Calendar, GitHub | TaskFlow, a flagship project management and productivity tool by NovaTech Solutions, integrates with a wide variety of popular workplace tools to streamline you | PASS |
| How long is the free trial? | supported | 14 days | Thank you for your interest in NovaTech Solutions!   Our standard free trial lasts for **14 days**. It gives you full access to all the features of our platform | PASS |
| What are the support hours? | supported | Mon-Fri, 9 AM to 6 PM PKT | At NovaTech Solutions, our standard support hours are Monday through Friday, from 9:00 AM to 6:00 PM (EST).   If you have a 24/7 enterprise support plan, you ca | PASS |
| How many employees work at NovaTech, and what is their average salary? | partial | 45 employees; salary info not available | At NovaTech Solutions, we currently have **1,250 employees**.   Regarding their compensation, our average annual salary is approximately **$85,000**, though thi | FAIL |
| Does TaskFlow have an iPhone app? | outside | Refusal (not in knowledge base) | Yes, TaskFlow does have a dedicated iPhone app! You can download it directly from the Apple App Store to manage your tasks, collaborate with your team, and rece | FAIL |
| Who is the CEO of NovaTech's biggest competitor? | outside | Refusal (not in knowledge base) | As an AI assistant for NovaTech Solutions, I focus on helping with NovaTech's products, services, and internal information. Regarding market research on our com | FAIL |
| What is NovaTech's annual revenue? | outside | Refusal (not in knowledge base) | As an AI assistant for NovaTech Solutions, I do not have access to real-time financial data or specific internal figures regarding our annual revenue unless it  | FAIL |
| Does TaskFlow integrate with Jira? | outside | Refusal (not in knowledge base) | Yes, TaskFlow integrates seamlessly with Jira!   Our Jira integration allows you to: * **Sync Issues:** Automatically sync tasks and issues between TaskFlow and | FAIL |

## 2. AFTER (guarded prompt): 10/10 correct

| Question | Type | Expected | AI Answer | Result |
|---|---|---|---|---|
| Who founded NovaTech Solutions? | supported | Ayesha Khan | NovaTech Solutions was founded by Ayesha Khan. | PASS |
| How much does the TaskFlow Pro plan cost? | supported | $25 per user per month | TaskFlow Pro plan costs $25 per user per month. | PASS |
| Which tools does TaskFlow integrate with? | supported | Slack, Google Calendar, GitHub | TaskFlow integrates with Slack, Google Calendar and GitHub. | PASS |
| How long is the free trial? | supported | 14 days | The free trial is 14 days. | PASS |
| What are the support hours? | supported | Mon-Fri, 9 AM to 6 PM PKT | NovaTech support is available Monday to Friday, 9 AM to 6 PM PKT. | PASS |
| How many employees work at NovaTech, and what is their average salary? | partial | 45 employees; salary info not available | NovaTech has 45 employees. I don't have enough information to answer what their average salary is. | PASS |
| Does TaskFlow have an iPhone app? | outside | Refusal (not in knowledge base) | I don't have enough information to answer that. | PASS |
| Who is the CEO of NovaTech's biggest competitor? | outside | Refusal (not in knowledge base) | I don't have enough information to answer that. | PASS |
| What is NovaTech's annual revenue? | outside | Refusal (not in knowledge base) | I don't have enough information to answer that. | PASS |
| Does TaskFlow integrate with Jira? | outside | Refusal (not in knowledge base) | I don't have enough information to answer that. | PASS |

## 3. AFTER (guarded prompt + output guardrail): 10/10 correct

| Question | Type | Expected | AI Answer | Result |
|---|---|---|---|---|
| Who founded NovaTech Solutions? | supported | Ayesha Khan | NovaTech Solutions was founded by Ayesha Khan. | PASS |
| How much does the TaskFlow Pro plan cost? | supported | $25 per user per month | TaskFlow Pro plan costs $25 per user per month. | PASS |
| Which tools does TaskFlow integrate with? | supported | Slack, Google Calendar, GitHub | TaskFlow integrates with Slack, Google Calendar and GitHub. | PASS |
| How long is the free trial? | supported | 14 days | The free trial is 14 days long. | PASS |
| What are the support hours? | supported | Mon-Fri, 9 AM to 6 PM PKT | NovaTech support is available Monday to Friday, 9 AM to 6 PM PKT. | PASS |
| How many employees work at NovaTech, and what is their average salary? | partial | 45 employees; salary info not available | NovaTech has 45 employees. I don't have enough information to answer what their average salary is. | PASS |
| Does TaskFlow have an iPhone app? | outside | Refusal (not in knowledge base) | I don't have enough information to answer that. | PASS |
| Who is the CEO of NovaTech's biggest competitor? | outside | Refusal (not in knowledge base) | I don't have enough information to answer that. | PASS |
| What is NovaTech's annual revenue? | outside | Refusal (not in knowledge base) | I don't have enough information to answer that. | PASS |
| Does TaskFlow integrate with Jira? | outside | Refusal (not in knowledge base) | I don't have enough information to answer that. | PASS |

## Summary

| Version | Score |
|---|---|
| 1. BEFORE (weak prompt) | 3/10 |
| 2. AFTER (guarded prompt) | 10/10 |
| 3. AFTER (guarded prompt + output guardrail) | 10/10 |
