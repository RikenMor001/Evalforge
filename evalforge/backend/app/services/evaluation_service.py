from app.benchmarks.loader import load_benchmark
from app.runners.base import BaseModelRunner
from app.evaluators.base import BaseEvaluator

def run_evalutaion(
    benchmark_filename: str,
    runner: BaseModelRunner,
    evaluator: BaseEvaluator
) -> dict:
    benchmark = load_benchmark(benchmark_filename)

    results = {}

    for case in benchmark.cases:

        # Get the prompt from benchmark
        prompt = case.prompt

        # Run the prompt through the model
        model_output = runner.run(prompt)

        # Evaluate the model after running
        evaluation = evaluator.evaluate(
            expected_output=case.expected_output,
            actual_output = model_output
        )

        # Store the result and return it 
        results[case.id] = {
            "prompt": prompt,
            "expected_output": case.expected_output,
            "model-output": model_output,
            "evaluator": evaluation
        }

    return results