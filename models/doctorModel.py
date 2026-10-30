from pydantic import BaseModel
from typing import Optional


class Doctor(BaseModel):
    id: Optional[str] = None
    name: str
    specialization: str
    salary: float
