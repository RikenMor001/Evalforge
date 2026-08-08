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

def generate(self, prompt: str) -> ModelResponse:
    start_time = time.perf_counter()

    answer = self.answers.get(
        prompt,
        "I do not know"
    )

    latency_ms = (
        time.perf_counter - start_time
    ) * 1000

    return ModelResponse(
        text=answer,
        latency_ms=latency_ms
    )