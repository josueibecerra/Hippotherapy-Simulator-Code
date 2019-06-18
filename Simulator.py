# import modules
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
from tkinter import *


# set up weight sensors
def weight_sensor():
    GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
    hx = HX711(dout_pin=21, pd_sck_pin=20)  # create an object
    print(hx.get_raw_data_mean())  # get raw data reading from hx711
    GPIO.cleanup()
    return int(hx.get_raw_data_mean())  # returns the measured weight when ran


weight = weight_sensor()  # names weight and puts the number into your function; WON'T be used in final code


# set up motors


# Start of GUI
win = Tk()


