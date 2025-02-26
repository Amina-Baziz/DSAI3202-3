import time
from src. functions import initialize_display, latest_temperatures ,temperature_averages
from src.threads import create_threads


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
            sensor_temps = ' '.join(f"Sensor {i+1}: {latest_temperatures.get(i, '--')}°C" for i in range(3))
            avg_temps = ' '.join(f"Sensor {i+1} Average: {temperature_averages.get(i, '--')}°C" for i in range(3))

           
            sys.stdout.write("\033[F" * 4)  
            sys.stdout.write("\033[K") 
            print(f"Latest Temperatures: {sensor_temps}")
            print(f"Sensor 1 Average: {temperature_averages.get(0, '--')}°C")
            print(f"Sensor 2 Average: {temperature_averages.get(1, '--')}°C")
            print(f"Sensor 3 Average: {temperature_averages.get(2, '--')}°C")

            sys.stdout.flush()  
        time.sleep(interval)


def main():
    initialize_display()
    create_threads()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram terminated.")

if __name__ == "__main__":
    main()
