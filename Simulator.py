# import modules
import time
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
from tkinter import *


# set up weight sensors
def measure_weight():
    try:
        GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
        hx = HX711(dout_pin=21, pd_sck_pin=20)  # create an object
        hx.get_raw_data_mean()  # get raw data reading from hx711
        GPIO.cleanup()
        return int(hx.get_raw_data_mean())  # returns the measured weight when ran
    except FileNotFoundError:
        print('File Not Found Error: Weight Not Measured')


# set up motors and run motors;
def init_motors():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
    except FileNotFoundError:
        print('File Not Found Error: Could Not Initiate Motors')


def start_motors():  # runs motors relative to weight; replace later with excel formula
    try:
        init_motors()
        motor1 = GPIO.PWM(7, 100)  # 100 is the frequency
        motor2 = GPIO.PWM(11, 100)
        while 0 <= measure_weight() * output_control <= 100:
            motor1.start(measure_weight() * output_control)  # number in parentheses must be a percent of power output
            motor2.start(measure_weight() * output_control)
        else:
            motor1.start(100)
            motor2.start(100)
        GPIO.cleanup()
        print('Motors Started')
    except AttributeError:
        print('Attribute Error: Could Not Start Motors (Likely PWM not found)')
    except FileNotFoundError:
        print('File Not Found: Could Not Start Motors')


def stop_motors():
    try:
        init_motors()
        motor1 = GPIO.PWM(7, 100)
        motor2 = GPIO.PWM(11, 100)
        motor1.start(0)
        motor2.start(0)
        print('Motors Stopped')
    except AttributeError:
        print('Attribute Error: Could Not Stop Motors (Likely PWM not found)')
    except FileNotFoundError:
        print('File Not Found Error: Could Not Stop Motors')


output_control = 0.5  # runs motors at half of the persons weight; Will be adjusted

# Start of GUI
root = Tk()

start_button = Button(root, text='START', bg='grey', command=start_motors)
stop_button = Button(root, text='STOP', bg='red', command=stop_motors)
start_button.pack()
stop_button.pack()

root.mainloop()
