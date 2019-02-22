from tkinter import *

win = Tk()

name = Label(win,text = "name")
password = Label(win,text ="password")
email = Label(win,text = "email")

entry1 = Entry(win)
entry2 = Entry(win)
entry3 = Entry(win)

name.grid(row=0)
password.grid(row=1)
email.grid(row=2)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)

check = Checkbutton(win,text="keep me login")
check.grid(columnspan=2)

win.mainloop()