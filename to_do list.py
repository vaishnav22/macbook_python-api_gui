from tkinter import *

list = ["add vegies"]
win = Tk()
win.geometry("250x350")
win.title("ToDo List")
lable1 =  Label(win, text = 'To Do List')
lable1.pack()

entry1 = Entry(win,width = 30)
entry1.pack()

def update_list():
    for task in list:
        lable_tasks.insert("end",task)

def clear_list():
    lable_tasks.delete(0,"end")


def add_task():
    update_list()

def del_task():
    pass

def del_all_task():
    clear_list()

def no_task():
    pass

def exit_task():
    pass

but_add_task = Button(win, text = "Add Task", fg = "green",bg ="white",command = add_task)
but_add_task.pack()

but_del_task = Button(win, text = "Delete ", fg = "green",bg ="white",command = del_task)
but_del_task.pack()

but_delall_task = Button(win, text = "Delete All", fg = "green",bg ="white",command = del_all_task)
but_delall_task.pack()

but_no_of_task = Button(win, text = "Number of Task", fg = "green",bg ="white",command = no_task)
but_no_of_task.pack()

but_exit_task = Button(win, text = "quit", fg = "green",bg ="white",command = exit_task)
but_exit_task.pack()






















lable_tasks = Listbox(win)
lable_tasks.pack()
win.mainloop()

