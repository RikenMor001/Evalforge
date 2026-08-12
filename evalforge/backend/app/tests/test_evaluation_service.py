from types import SimpleNamespace

class MockRunner:
    def run(self, prompt: str) -> str:
        return "100"

class MockEvaluator:
    def evaluate(self, expected: str, actual: str) -> str:
        passed = expected == actual

        return {
            "score": 1.0 if passed else 0.0,
            "passed": passed
        }

def run_evaluation():
    fake_benchmark = SimpleNamespace(
        cases = [
            SimpleNamespace(
                id="math_1",
                prompt = "What is 10+90",
                expected_output = "100"
            )
        ]
    )

    runner = MockRunner()
    evaluator = MockEvaluator()