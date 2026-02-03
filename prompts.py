SYSTEM_PROMPT = """
You are an expert interview coach.

Rules:
- Follow the difficulty level strictly.
- Do NOT repeat previous questions.
- Each answer must be 4–5 lines.
- Use realistic interview tone.
- Output valid JSON only.
"""

def difficulty_rules(level):
    return {
        "junior": "Basic concepts, definitions, simple examples.",
        "mid": "Practical usage, trade-offs, real-world scenarios.",
        "senior": "System design, scaling, edge cases.",
        "staff": "Architecture decisions, leadership, ambiguity handling."
    }[level]

def generate_prompt(jd, previous_questions, difficulty):
    return f"""
JOB DESCRIPTION:
{jd}

DIFFICULTY:
{difficulty.upper()}
{difficulty_rules(difficulty)}

PREVIOUS QUESTIONS:
{previous_questions}

TASK:
Generate 10–15 NEW interview questions.
Do NOT repeat earlier questions.

Output format:
{{
  "questions": [
    {{
      "question": "...",
      "answer": "..."
    }}
  ]
}}
"""
