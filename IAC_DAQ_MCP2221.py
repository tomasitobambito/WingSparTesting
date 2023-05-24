# Just in case the environment variables were not properly set
import os
os.environ["BLINKA_MCP2221"] = "1"
os.environ["BLINKA_MCP2221_RESET_DELAY"] = "-1"

import board
import busio
import time

import adafruit_vl53l0x
from cedargrove_nau7802 import NAU7802

gradient = -0.001105893
offset = -139.7849128


def save_data(filename, timestamp, distance, load):
    '''
    Save sensor data to text file. 
    '''
    with open(filename, "a") as file:
        file.write(str(timestamp)+","+str(distance)+","+str(load)+"\n")


def return_calibrated(value, gradient, offset):
    '''
    Calibrates sensor readings using a linear approximation
    '''
    return (gradient * value) + offset


# Load cell
loadCellSensor = NAU7802(board.I2C(), address=0x2a, active_channels=1)

# Time of flight sensor
i2c = busio.I2C(board.SCL, board.SDA)
tofSensor = adafruit_vl53l0x.VL53L0X(i2c)

print("Starting measurements. \n")

# Perform measurements
try:
    while True:
        # Get sensor readings
        loadCellValue = loadCellSensor.read()
        tofValue = tofSensor.range
        timestamp = time.time()

        loadCellCalibratedValue = return_calibrated(loadCellValue, gradient, offset)

        save_data("out.txt", timestamp, tofValue, loadCellCalibratedValue)

        # Output sensor data
        print("Load cell: {:.0f}, Distance: {:.0f}".format(loadCellCalibratedValue, tofValue))
        # print("Load cell: {:.0f}".format(loadCellValue))

        # Sleep
        time.sleep(1)

# Exit
except KeyboardInterrupt:
    print("\nexiting...\n")
