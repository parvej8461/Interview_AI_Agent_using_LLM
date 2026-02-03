import json
from groq_client import call_groq
from prompts import SYSTEM_PROMPT, generate_prompt

class InterviewAgent:

    def __init__(self, memory):
        self.memory = memory

    def run(self, session_id, job_description, difficulty):

        state = self.memory.get(session_id)

        if not state:
            state = {
                "job_description": job_description,
                "difficulty": difficulty,
                "questions": [],
                "round": 1
            }

        prompt = generate_prompt(
            jd=state["job_description"],
            previous_questions=state["questions"],
            difficulty=state["difficulty"]
        )

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]

        raw_output = call_groq(messages)
        parsed = json.loads(raw_output)

        new_questions = parsed["questions"]

        state["questions"].extend(
            [q["question"] for q in new_questions]
        )
        state["round"] += 1

        self.memory.save(session_id, state)

        return {
            "round": state["round"],
            "difficulty": state["difficulty"],
            "questions": new_questions
        }
