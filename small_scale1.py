import RPi.GPIO as GPIO
import time
import tkinter as tk

rpm = 0
power_output=0
sensor = 40  # define the GPIO pin our sensor is attached to

sample = 20  # how many half revolutions to time
count = 0

start = 0
end = 0

desired_rpm = 1500


GPIO.setmode(GPIO.BOARD)  # set GPIO numbering system to BOARD
GPIO.setup(sensor, GPIO.IN)  # set our sensor pin to an input


GPIO.setup(7, GPIO.OUT)

p= GPIO.PWM(7, 207)

p.start(0)


def set_start():
    global start
    start = time.time()


def set_end():
    global end
    end = time.time()


def get_rpm(c):
    global count  # delcear the count variable global so we can edit it

    if not count:
        set_start()  # create start time
        count = count + 1  # increase counter by 1
    else:
        count = count + 1

    if count == sample:
        global rpm
        set_end()  # create end time
        delta = end - start  # time taken to do a half rotation in seconds
        delta = delta / 60  # converted to minutes
        rpm = (sample / delta) / 2  # converted to time for a full single rotation
        print(rpm)
        count = 0  # reset the count to 0



def start_program():
    GPIO.add_event_detect(sensor, GPIO.RISING,
                      callback=get_rpm)  # execute the get_rpm function when a HIGH signal is detected
    global power_output
    global desired_rpm

    try:
        while True:  # create an infinite loop to keep the script running
            if desired_rpm >= rpm and power_output<100:
                power_output=power_output+1
                p.ChangeDutyCycle(power_output)
                time.sleep(0.5)
            if desired_rpm <= rpm and power_output>0:
                power_output=power_output-1
                p.ChangeDutyCycle(power_output)
                time.sleep(0.5)
    except KeyboardInterrupt:
        print('Quit')
        GPIO.cleanup()
        pass

    p.stop()


def stop_program():
    try:
        p.stop()
        GPIO.Cleanup
    except KeyboardInterrupt:
        print('Quit')
        GPIO.cleanup()
        pass


# Start of GUI
root = tk.Tk()

root.geometry('480x320')

start_button = tk.Button(root, text='START', bg='grey', command=start_program, font=('Times', 40))
stop_button = tk.Button(root, text='STOP', bg='red', command=stop_program, font=('Times', 40))
start_button.pack(side='top', expand=True, fill='both')
stop_button.pack(side='bottom', expand=True, fill='both')

root.mainloop()
