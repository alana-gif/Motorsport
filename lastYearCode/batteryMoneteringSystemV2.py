import time
import random
from threading import Thread, Event
# Constants
DELAY_S = 3
MAX_TEMP = 60
NUM_CELLS = 4


# Avoid race conditions
keep_running = Event()
keep_running.set()

# Worker thread to monitor the cells
def monitor_worker(keep_running):
    while keep_running.is_set():
        print("Monitoring Battery Cells...\n")
        for cell_index in range(NUM_CELLS):
            temperature = 25 + random.uniform(-5, 80) # Dummy Data: 
            temperature
            voltage = 3.7 + random.uniform(-0.1, 0.1) # Dummy Data: 
            voltage
            current = 0.5 + random.uniform(-0.2, 0.2) # Dummy Data: 
            current
            percentage = (voltage - 3.0) / (4.2 - 3.0) * 100 # Dummy Data: battery percentage
            # Print out the values for each cell
            print(f"Cell {cell_index + 1}:")
            print(f" Temp: {temperature:.2f} °C, Voltage: {voltage:.2f} V, Current: {current:.2f} A, Battery: {percentage:.2f}%\n")
    time.sleep(30)
# Worker thread to check for user input
def keypress_worker(keep_running):
 input("Press ENTER to stop monitoring...\n")
 keep_running.clear()
 print("User requested stop. Exiting monitor...")
# Function to start both threads
def start_threads():
    monitor_thread = Thread(target=monitor_worker, 
    args=(keep_running,))
    keypress_thread = Thread(target=keypress_worker, 
    args=(keep_running,))
    monitor_thread.start()
    keypress_thread.start()
    monitor_thread.join()
    keypress_thread.join()
# Main Program
print("Starting program...")

start_threads()

print("Program exited.")
