from tkinter import *

items = []

class Myclass():
    def __init__(self,win):
        frame = Frame(win)
        frame.pack()


        self.button = Button(win, text = "Vegitables", fg="green",command = self.printMsg)
        self.button.pack()

        self.button2 = Button(win , text = "Non veg",fg = "red")
        self.button2.pack()

    def printMsg(self):
        print("this is working")


win = Tk()
win.title("shopping cart")
win.geometry("500x500")
vai = Myclass(win)








win.mainloop()