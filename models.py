from pydantic import BaseModel
from typing import Optional
from enums import Difficulty

class InterviewRequest(BaseModel):
    session_id: str
    job_description: Optional[str] = None
    difficulty: Difficulty = Difficulty.mid
