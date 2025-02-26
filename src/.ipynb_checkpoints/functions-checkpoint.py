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

def initialize_display():
    """Prints the initial layout for displaying temperatures."""
    print("Current temperatures:")
    print("Latest Temperatures: Sensor 1: --°C Sensor 2: --°C Sensor 3: --°C")
    print("Sensor 1 Average: --°C")
    print("Sensor 2 Average: --°C")
    print("Sensor 3 Average: --°C")



def update_display(interval=5):
    """Updates the temperature display in-place without misalignment issues."""
    while True:
        with lock:
            # Prepare formatted temperature strings
            sensor_temps = ' '.join(f"Sensor {i+1}: {latest_temperatures.get(i, '--')}°C" for i in range(3))
            avg_temps = ' '.join(f"Sensor {i+1} Average: {temperature_averages.get(i, '--')}°C" for i in range(3))

            # Move cursor up and clear previous output properly
            sys.stdout.write("\033[F" * 4)  # Move cursor up by 4 lines
            sys.stdout.write("\033[K")  # Clear current line
            print(f"Latest Temperatures: {sensor_temps}")
            print(f"Sensor 1 Average: {temperature_averages.get(0, '--')}°C")
            print(f"Sensor 2 Average: {temperature_averages.get(1, '--')}°C")
            print(f"Sensor 3 Average: {temperature_averages.get(2, '--')}°C")

            sys.stdout.flush()  # Force update to console
        time.sleep(interval)
