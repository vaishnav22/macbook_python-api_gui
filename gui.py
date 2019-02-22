from tkinter import *

win = Tk()
win.geometry("200x100")
name = Label(win, text = "Name")
password = Label(win, text = "Password")
email = Label(win, text = "Email")

name.grid(row=0)
password.grid(row=1)
email.grid(row=2)

entry1= Entry(win)
entry2= Entry(win)
entry3= Entry(win)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

check = Checkbutton(win,text="keep me logged in")

check.grid(columnspan = 2)

win.mainloop()