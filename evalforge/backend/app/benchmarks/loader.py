import json
from pathlib import Path
from app.schemas.benchmark import BenchMark

DATASET_DIRECTORY = Path(__file__).parent/"datasets"

def load_benchmark(filename: str) -> BenchMark:
    benchmark_path = DATASET_DIRECTORY / f"{filename}.json"

    if not benchmark_path.exists():
        raise FileNotFoundError(
            f"Benchmark '{filename}' was not found"
        )
    
    with benchmark_path.open("r", encoding="utf-8") as file:
        benchmark_data = json.load(file)

    return BenchMark.model_validate(benchmark_data)