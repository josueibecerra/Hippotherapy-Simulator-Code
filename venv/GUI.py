from tkinter import *


def start():
    print('Started')


def stop():
    print('Stopped')


root = Tk()

start_button = Button(root, text='START', bg='grey', command=start)
stop_button = Button(root, text='STOP', bg='red', command=stop)
start_button.pack()
stop_button.pack()

root.mainloop()
