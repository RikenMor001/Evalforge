from app.evaluators.exact_match import ExactmatchEvaluator

evaluator = ExactmatchEvaluator()

result = evaluator.evaluate(
    prediction = "20",
    expected_output = "20"
)

print (f"The resulted output: {result}")