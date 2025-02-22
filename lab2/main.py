# main.py

from src.model import (sequential_execution, thread_execution, process_execution)
from src.evaluation import (speedup, efficiency, amdahl_speedup, gustafson_speedup)

def print_performance_metrics(seq_time, exec_time, num_threads, label):
    sp = speedup(seq_time, exec_time)
    eff = efficiency(sp, num_threads)
    amdahl_sp = amdahl_speedup(0.5, num_threads)
    gustafson_sp = gustafson_speedup(0.5, num_threads)

    print(f'\n{label}')
    print(f'Execution time: {exec_time:.4f} seconds')
    print(f'Speedup: {sp:.2f}')
    print(f'Efficiency: {eff:.2f}')
    print(f'Amdahl’s Law Speedup: {amdahl_sp:.2f}')
    print(f'Gustafson’s Law Speedup: {gustafson_sp:.2f}')

def main():
    seq_time = sequential_execution()
    thread_time = thread_execution()
    process_time = process_execution()

    print_performance_metrics(seq_time, seq_time, 1, "Sequential Execution ")
    print_performance_metrics(seq_time, thread_time, 2, "Threaded Execution ")
    print_performance_metrics(seq_time, process_time, 2, "Process Execution ")

if __name__ == '__main__':
    main()
