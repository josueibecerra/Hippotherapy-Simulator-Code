# import modules
import time
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
import tkinter as tk


# set up break beam sensors
sensor = 21  # define the GPIO pin our sensor is attached to

GPIO.setmode(GPIO.BCM)  # set GPIO numbering system to BCM
GPIO.setup(sensor, GPIO.IN)  # set our sensor pin to an input

sample = 10  # how many half revolutions to time
count = 0

start = 0
end = 0


def set_start():
    global start
    start = time.time()


def set_end():
    global end
    end = time.time()


def get_rpm():
    global count  # declare the count variable global so we can edit it

    if not count:
        set_start()  # create start time
        count = count + 1  # increase counter by 1
    else:
        count = count + 1

    if count == sample:
        set_end()  # create end time
        delta = end - start  # time taken to do a half rotation in seconds
        delta = delta / 60  # converted to minutes
        rpm = (sample / delta) / 2  # converted to time for a full single rotation
        print(rpm)
        count = 0  # reset the count to 0


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
    finally:
        GPIO.cleanup()
        pass


# set up motors and run motors;
def init_motors():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.add_event_detect(sensor, GPIO.RISING,
                              callback=get_rpm)  # execute the get_rpm function when a HIGH signal is detected
    except FileNotFoundError:
        print('File Not Found Error: Could Not Initiate Motors')
    finally:
        pass


def start_motors():  # runs motors relative to weight; replace later with excel formula
    global motors_started  # allows variables to be referenced within a function
    if motors_started:
        print('Motors Already Started')
    else:
        try:
            init_motors()
            motor1 = GPIO.PWM(7, 100)  # 100 is the frequency
            motor2 = GPIO.PWM(11, 100)
            while 0 <= measure_weight() * output_control <= 100:
                motor1.start(
                    measure_weight() * output_control)  # number in parentheses must be a percent of power output
                motor2.start(measure_weight() * output_control)
            else:
                motor1.start(100)
                motor2.start(100)
            GPIO.cleanup()
            motors_started = True
            print('Motors Started')
        except AttributeError:
            motors_started = False
            print('Attribute Error: Could Not Start Motors (Likely PWM not found)')
        except FileNotFoundError:
            motors_started = False
            print('File Not Found: Could Not Start Motors')
        finally:
            GPIO.cleanup()
            pass


def stop_motors():
    global motors_started
    if not motors_started:
        print('Motors Already Stopped')
    else:
        try:
            init_motors()
            motor1 = GPIO.PWM(7, 100)
            motor2 = GPIO.PWM(11, 100)
            motor1.start(0)
            motor2.start(0)
            print('Motors Stopped')
            motors_started = False
        except AttributeError:
            print('Attribute Error: Could Not Stop Motors (Likely PWM not found)')
        except FileNotFoundError:
            print('File Not Found Error: Could Not Stop Motors')
        finally:
            GPIO.cleanup()
            pass


# Initial Conditions Set
output_control = 0.5  # runs motors at half of the persons weight; Will be adjusted
motors_started = False  # initial state of the motors is not started; 1:40:00


# Start of GUI
root = tk.Tk()

root.geometry('480x320')

start_button = tk.Button(root, text='START', bg='grey', command=start_motors, font=('Times', 40))
stop_button = tk.Button(root, text='STOP', bg='red', command=stop_motors, font=('Times', 40))
start_button.pack(side='top', expand=True, fill='both')
stop_button.pack(side='bottom', expand=True, fill='both')

root.mainloop()
