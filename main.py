from fastapi import FastAPI
from models import InterviewRequest
from memory import InterviewMemory
from agent import InterviewAgent

app = FastAPI(title="Interview Assistant Agent")

memory = InterviewMemory()
agent = InterviewAgent(memory)

@app.post("/interview")
def interview(request: InterviewRequest):

    result = agent.run(
        session_id=request.session_id,
        job_description=request.job_description,
        difficulty=request.difficulty.value
    )

    return result
