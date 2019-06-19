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


# set up motors and run motors;
def init_motors():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)


def start_motors(tf, output_control):  # runs motors relative to weight; replace later with excel formula
    init_motors()
    motor1 = GPIO.PWM(7, 100)
    motor2 = GPIO.PWM(11, 100)
    while measure_weight()*output_control() >= 100:
        motor1.start(measure_weight()*output_control())  # number in parentheses must be a percent of power output
        motor2.start(measure_weight()*output_control())
    else:
        motor1.start(100)
        motor2.start(100)
    time.sleep(tf)
    GPIO.cleanup()


start_motors(20, 0.5)  # NOT in final code; runs motors for 20 seconds at half of the persons weight


# Start of GUI
win = Tk()
