from app.benchmarks.loader import load_benchmark

benchmark = load_benchmark("arithmetic")

print(
    benchmark.name, 
    benchmark.description, 
    benchmark.version,
    f"Tasks: {len(benchmark.tasks)}"
)

for task in benchmark.tasks:
    print(task.id, task.prompt, task.expected_answer)