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