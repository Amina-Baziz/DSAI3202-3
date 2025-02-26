import threading
from src.functions import simulate_sensor, process_temperatures, update_display

def create_threads():
    """Creates and starts threads for sensor simulation, data processing, and display update."""
    sensor_threads = [threading.Thread(target=simulate_sensor, args=(i,)) for i in range(3)]
    process_thread = threading.Thread(target=process_temperatures)
    display_thread = threading.Thread(target=update_display, daemon=True)

    threads = sensor_threads + [process_thread, display_thread]
    for thread in threads:
        thread.start()

    return threads
