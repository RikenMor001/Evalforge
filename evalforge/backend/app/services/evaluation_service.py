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