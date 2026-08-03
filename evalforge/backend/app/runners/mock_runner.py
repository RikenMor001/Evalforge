import time

from app.runners.base import ModelResponse, BaseModelRunner

class BaseModelRunner(BaseModelRunner):

    answers = {
        "What is 12 + 8? Return only the number. ": "20",
        "What is 7 multiplied by 6? Return only the number. ": "42",
        "What is 100 divided by 10? Return only the number" : "10"
    }

@property
def model_name(self) -> str:
    return "mock-model-v1"