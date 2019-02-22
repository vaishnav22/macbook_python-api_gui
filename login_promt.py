from tkinter import *
import tkinter.messagebox



win = Tk()
win.geometry("300x300")
win.title("Login Prompt")

def show_messg():
    user = entry1.get()
    passwrd = entry2.get()
    if user == "vaishnav" and passwrd == "123":
        tkinter.messagebox.showinfo('Window title', 'Sucessfully Logged In!!')

name = Label(win,text = "Name")
password = Label(win,text = "Password")

name.grid(row = 0)
password.grid(row=1)

entry1 =Entry(win)
entry2 =Entry(win)

entry1.grid(row =0,column = 1)
entry2.grid(row =1,column = 1)


check = Checkbutton(win,text="keep me logged in")
check.grid(columnspan = 2)

button1 = Button(win,text = "Login",command = show_messg)
button1.grid(row = 3,column = 1)








win.mainloop()