# import modules
import time
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
from tkinter import *


# set up weight sensors
def measure_weight():
    GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
    hx = HX711(dout_pin=21, pd_sck_pin=20)  # create an object
    hx.get_raw_data_mean()  # get raw data reading from hx711
    GPIO.cleanup()
    return int(hx.get_raw_data_mean())  # returns the measured weight when ran


print(measure_weight())  # NOT in final code; returns weight sensor value; code skips over def weight_sensor(): till now


# set up motors


# Start of GUI
win = Tk()
