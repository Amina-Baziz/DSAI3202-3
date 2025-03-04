
from src.evaluation import evaluate_performance

if __name__ == "__main__":
    large_number = 10**6
    num_threads = 4
    num_processes = 4

    evaluate_performance(large_number, num_threads, num_processes)
