# src/evaluation.py

def speedup(sequential_time, parallel_time):
    return sequential_time / parallel_time if parallel_time > 0 else float('inf')

def efficiency(speedup_value, num_threads):
    return speedup_value / num_threads if num_threads > 0 else 0

def amdahl_speedup(p, num_threads):
    return 1 / ((1 - p) + (p / num_threads))

def gustafson_speedup(p, num_threads):
    return num_threads - (1 - p) * num_threads
