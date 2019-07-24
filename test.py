import tkinter as tk
import time

running = False


def scanning_rpm():
    if running:
        print('Checking RPM')
    root.after(1000, scanning_rpm)


def start_motors():
    global running
    running = True
    print('motors running')


def stop_motors():
    global running
    running = False
    print('motors stopped')


# Start of GUI
root = tk.Tk()

root.geometry('480x320')

start_button = tk.Button(root, text='START', bg='grey', command=start_motors, font=('Times', 40))
stop_button = tk.Button(root, text='STOP', bg='red', command=stop_motors, font=('Times', 40))
start_button.pack(side='top', expand=True, fill='both')
stop_button.pack(side='bottom', expand=True, fill='both')

root.after(1000, scanning_rpm)

root.mainloop()
