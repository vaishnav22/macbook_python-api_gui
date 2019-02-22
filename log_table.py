from tkinter import *
import math


def show_data():
    textname = int(entry.get())
    log_ans = math.log10(textname)
    label = Label(win,text = log_ans).pack()


win = Tk()

win.geometry("300x450")
win.title("Log Table")
label1 = Label(win, text = "value").pack()



entry = Entry(win)
entry.pack()
button1 = Button(win,text = "convert",command = show_data).pack()




win.mainloop()