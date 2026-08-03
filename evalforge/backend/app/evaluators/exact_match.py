from app.evaluators.base import BaseEvaluator, EvaluationScore

class ExactmatchEvaluator(BaseEvaluator):
    def evaluate(
        self,
        prediction: str,
        expected_output: str
    ) -> EvaluationScore:
        normalized_prediction = prediction.strip().lower()
        normalized_output = expected_output.strip().lower()

        passed = normalized_prediction == normalized_output

        return EvaluationScore(
            score = 1.0 if passed else 0.0, # score has to be 1 if the passed value goes through
            # which is only if the passed value is true (because it's a boolean) should 
            # the variable return 1.0 or else return 0.0
            passed=passed,
            reason=(
                "The model matched the expected output."
                if passed
                else "The predicted output was not the same as the real output."
            )
        )