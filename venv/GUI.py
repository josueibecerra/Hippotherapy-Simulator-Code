from tkinter import *


def start():
    print('Started')


def stop():
    print('Stopped')


root = Tk()

start_button = Button(root, text='START', bg='grey', command=test)
stop_button = Button(root, text='STOP', bg='red', command=test2)
start_button.pack()
stop_button.pack()

root.mainloop()
