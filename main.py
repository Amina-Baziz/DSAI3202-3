from src.sequential import execution_time_seq
from src.parallel import execution_time_par
from src.parallel import num_workers

print(f"Sequential execution time: {execution_time_seq} seconds")
print(f"Optimized Parallel execution time: {execution_time:.2f} seconds")

speedup = execution_time_seq / execution_time_par
efficiency = speedup / num_workers

print(f"Speedup: {speedup:.2f}")
print(f"Efficiency: {efficiency:.2f}")
