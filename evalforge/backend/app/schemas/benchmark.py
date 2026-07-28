from pydantic import BaseModel, Field

class BenchMark(BaseModel):
    id: str
    prompt: str
    expected_answer: str

class BenchMark(BaseModel):
    name: str