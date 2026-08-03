from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class ModelResponse:
    text: str
    latency_ms: float

class BaseModelRunner(ABC):

    @property
    @abstractmethod
    def model_name(self) -> str:
        pass

    @abstractmethod
    def generate(self, prompt: str) -> ModelResponse:
        pass