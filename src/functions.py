import random
import threading
import time
import queue
import sys


# Global data structures
latest_temperatures = {}
temperature_averages = {}
temperature_queue = queue.Queue()

# Locks and Condition for synchronization
lock = threading.RLock()
condition = threading.Condition(lock)


def simulate_sensor(sensor_id, interval=1):
    """Simulates temperature readings and updates the latest_temperatures dictionary."""
    while True:
        temperature = random.randint(15, 40)
        with lock:
            latest_temperatures[sensor_id] = temperature
            temperature_queue.put((sensor_id, temperature))
            condition.notify()  # Notify the processing thread
        time.sleep(interval)


def process_temperatures(interval=5):
    """Calculates the average temperature from queued readings."""
    while True:
        with lock:
            condition.wait()  # Wait for new data
            temp_data = {}

            while not temperature_queue.empty():
                sensor_id, temp = temperature_queue.get()
                if sensor_id not in temp_data:
                    temp_data[sensor_id] = []
                temp_data[sensor_id].append(temp)

            for sensor_id, temps in temp_data.items():
                avg_temp = sum(temps) / len(temps)
                temperature_averages[sensor_id] = avg_temp
        time.sleep(interval)


import sys

