#05
#a new program that watches each individual cell.
#brains cooked like a poached salmon right now

import time
import random

# Number of cells in the battery
NUM_CELLS = 4

while True:
    print("Monitoring Battery Cells...\n")

    for cell_index in range(NUM_CELLS):
        temperature = 25 + random.uniform(-5, 5)  # Dummy Data temperature between 20°C and 30°C
        voltage = 3.7 + random.uniform(-0.1, 0.1)  # Dummy Data voltage between 3.6V and 3.8V
        current = 0.5 + random.uniform(-0.2, 0.2)  # Dummy Data current between 0.3A and 0.7A
        percentage = (voltage - 3.0) / (4.2 - 3.0) * 100  # Battery percentage calculation based on voltage

        # Print out the values for each cell
        print(f"Cell {cell_index + 1}:")
        print(f"  Temp: {temperature:.2f} °C, Voltage: {voltage:.2f} V, Current: {current:.2f} A, Battery: {percentage:.2f}%\n")

    time.sleep(10)  # Wait 10 seconds before the next reading again

#ok no breakie wakie, no workie. you get an infinit loop or nothing
#this is shit
# the line above will spit an error when you kill the program because otherwise if you dont you are stuck in a long visouse loop you cant break.