in lab 3 we :
Build a data parallel model program using threads in Python
Build a data parallel model program using processes in Python
then For each case, compute:
 The speedup, The efficiency,The speedups using Amdhal’s Law,The speedups Gustaffson’s Law.
Execution time decreases from sequential to threaded to multiprocessing. Sequential takes the longest, threading offers slight improvement but is limited by Python’s GIL, and multiprocessing achieves the best performance by utilizing multiple CPU cores. Speedup and efficiency are analyzed using Amdahl’s and Gustafson’s laws. Challenges like workload distribution and process synchronization were managed through balanced workload and efficient memory use
