import time
import threading
import multiprocessing
from src.data_loader import generate_characters, generate_numbers

def sequential_execution():
    start = time.time()
    generate_characters()
    generate_numbers()
    end = time.time()
    return end - start

def thread_execution():
    start = time.time()
    t1 = threading.Thread(target=generate_characters)
    t2 = threading.Thread(target=generate_numbers)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    return end - start

def process_execution():
    start = time.time()
    p1 = multiprocessing.Process(target=generate_characters)
    p2 = multiprocessing.Process(target=generate_numbers)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    return end - start
