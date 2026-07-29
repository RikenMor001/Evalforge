from pydantic import BaseModel, Field

class BenchMarkTask(BaseModel):
    id: str
    prompt: str
    expected_answer: str

class BenchMark(BaseModel):
    name: str
    description: str
    version: str
    tasks: list[BenchMark]

class BenchMarkSummary(BaseModel):
    name: str
    description: str
    version: str
    task_count: int = Field(ge = 0)