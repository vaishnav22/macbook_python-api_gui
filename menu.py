from tkinter import *
import time;
import random;


win = Tk()

win.title("Billing Application")
win.geometry("850x600")

localtime = time.asctime(time.localtime(time.time()))

edli_vade = StringVar()
edli = StringVar()
masal = StringVar()
set_dosa = StringVar()
open_dosa = StringVar()
kara = StringVar()
chow = StringVar()
poori = StringVar()
coffe = StringVar()
tea = StringVar()




def total_ex():
    x = random.randint(0000, 3000)
    randomRef = str(x)
    ent11 = Label(win, text=randomRef)
    ent11.grid(row=2, column=1)

    a1 = int


    b1 = 55
    b2 = 30
    b3 = 65
    b4 = 60
    b5 = 65
    b6 = 30
    b7 = 30
    b8 = 40
    b9 = 15
    b10 = 15


    a1 = et1.get()
    a2 = ent2.get()
    a3 = et3.get()
    a4 = et4.get()
    a5 = ent5.get()
    a6 = ent6.get()
    a7 = ent7.get()
    a8 = ent8.get()
    a9 = ent9.get()
    a10 = ent10.get()


    c1 = (b1* a1)
    c2 = b2 * a2
    c3 = b3 * a3
    c4 = b4 * a4
    c5 = b5 * a5
    c6 = b6 * a6
    c7 = b7 * a7
    c8 = b8 * a8
    c9 = b9 * a9
    c10 = b10 * a10


    tot = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10

    total_ans = Label(win, text=tot)
    total_ans.grid(row=11, column=1)


def exit_1():
    win.destroy()


lb1 = Label(win, text="Amma's Kitchen\n", font="Denmark 16 bold", anchor='w')
lb1.grid(row=0, column=0)

lb2 = Label(win, text=localtime)
lb2.grid(row=1, column=0)

ref = Label(win, text="\nReference No\n", font="Denmark 12 bold")
ref.grid(row=2, column=0)

edli_vade = Label(win, text="\nEdli Vade\n", font="Denmark 12 bold")
edli_vade.grid(row=4, column=0)
ent2 = Entry()
ent2.grid(row=4, column=1)

edli = Label(win, text="Edli\n", font="Denmark 12 bold")
edli.grid(row=5, column=0)
et1 = Entry()
et1.grid(row=5, column=1)

masal = Label(win, text="Masale Dosa\n", font="Denmark 12 bold")
masal.grid(row=6, column=0)
et3 = Entry()
et3.grid(row=6, column=1)

set_dosa = Label(win, text="Set Dosa\n", font="Denmark 12 bold")
set_dosa.grid(row=7, column=0)
et4 = Entry()
et4.grid(row=7, column=1)

open_dosa = Label(win, text="Open Dosa\n", font="Denmark 12 bold")
open_dosa.grid(row=8, column=0)
ent5 = Entry()
ent5.grid(row=8, column=1)

kara = Label(win, text="\tKara Bath\n", font="Denmark 12 bold")
kara.grid(row=4, column=5)
ent6 = Entry()
ent6.grid(row=4, column=7)

chow = Label(win, text="\tChow Chow Bath\n", font="Denmark 12 bold")
chow.grid(row=5, column=5)
ent7 = Entry()
ent7.grid(row=5, column=7)

poori = Label(win, text="\tPoori\n", font="Denmark 12 bold")
poori.grid(row=6, column=5)
ent8 = Entry()
ent8.grid(row=6, column=7)

coffe = Label(win, text="\tCoffee\n", font="Denmark 12 bold")
coffe.grid(row=7, column=5)
ent9 = Entry()
ent9.grid(row=7, column=7)

tea = Label(win, text="\tTea\n", font="Denmark 12 bold")
tea.grid(row=8, column=5)
ent10 = Entry()
ent10.grid(row=8, column=7)

button1 = Button(win, text="TOTAL", command=total_ex)
button1.grid(row=10, column=1)

button3 = Button(win, text="Exit", command=exit_1)
button3.grid(row=10, column=7)

total = Label(win, text="\nTotal Amount")
total.grid(row=11, column=0)

win.mainloop()
