from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class EvaluationScore:
    score: float
    passed: bool
    reason: str

class BaseEvaluator(ABC):
    @abstractmethod
    def evaluate(
        self, 
        prediction: str,
        expected_output: str
    ) -> EvaluationScore:
        pass