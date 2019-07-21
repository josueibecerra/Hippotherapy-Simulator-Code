import tkinter as tk
import time


def start_motors():
    while True:
        print('motors running')
        time.sleep(0.1)


def stop_motors():
    while True:
        print('motors stopped')
        time.sleep(0.1)


# Start of GUI
root = tk.Tk()

root.geometry('480x320')

start_button = tk.Button(root, text='START', bg='grey', command=start_motors, font=('Times', 40))
stop_button = tk.Button(root, text='STOP', bg='red', command=stop_motors, font=('Times', 40))
start_button.pack(side='top', expand=True, fill='both')
stop_button.pack(side='bottom', expand=True, fill='both')

root.mainloop()
