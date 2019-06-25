from tkinter import *


def test():
    print('Test')


def test2():
    print('Test2')


root = Tk()

start_button = Button(root, text='START', bg='grey', command=test)
stop_button = Button(root, text='STOP', bg='red', command=test2)
start_button.pack()
stop_button.pack()

root.mainloop()
