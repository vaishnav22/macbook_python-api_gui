from tkinter import *


def fun():
    print("welcome to knowleade world")

def fun1():
    win1 = Tk()
    win.geometry("500x500")
    name=Label(win1,text = "welcome")
    name.pack()


win = Tk()

win.geometry("200x200")

button = Button(win,text = "click me" , command= fun1)
button.pack()

win.mainloop()