#  Interview Assistant Agent (LLM-Powered)

A **stateful interview preparation assistant** built using **FastAPI** and **Groq LLMs**.  
The system generates realistic interview questions based on a job description, supports difficulty levels, and remembers previous questions using an agent-based state machine.

---

##  Features
-  Stateful LLM agent (no repetition)
-  Difficulty selector (Junior → Staff)
-  Job-description driven questions
-  Multi-round interview sessions
-  Groq-powered ultra-fast inference
-  Clean, extensible architecture

---

##  Architecture Overview

Client
↓
FastAPI
↓
Interview Agent (State Machine)
↓
Memory Store (In-memory)
↓
Groq LLM


---

## Tech Stack

- Python 3.10+
- FastAPI
- Groq SDK
- Pydantic
- Uvicorn

---
# Example API Request
{
  "session_id": "session1",
  "job_description": "Hiring a Senior AI Engineer with LLM, FastAPI, and system design experience",
  "difficulty": "senior"
}

