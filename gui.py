import sys
import time
import datetime
import tkinter
from tkinter import messagebox
from tkinter import *
from random import randint

x = "500"
y = "100"
meret = x + "x" + y
now = datetime.datetime.now()
ido = str(now.hour) + " : " + str(now.minute)
top = tkinter.Tk()
top.geometry(meret)
top.resizable(0, 0)


def idoButton():
    messagebox.showinfo("Jelenlegi idő:", ido)


def LeszOKJ():
    leszE = messagebox.askyesno("O KÁ JÉ", "Lesz OKJ-m???")
    if leszE == True:
        messagebox.showinfo("yey", "Köszönööööm")
    if leszE == False:
        messagebox.showinfo("meh", "KAMU!")


def ablaknyitas():
    global meret
    jatek = tkinter.Tk()
    jatek.geometry(meret)
    game()


def game():
    gombJ = tkinter.Button(jatek, text="Kapj el", command=jatek.quit())
    i = 0
    while i < 10:
        gombJ.place(x=str(randint(0, int(x))), y=str(randint(0, int(y))))
        time.sleep(1)
        i = i+1
    jatek.mainloop()


gomb1 = tkinter.Button(top, text="OKJ", command=LeszOKJ)
gomb1.place(relx=0.0, rely=0.0, anchor="nw", bordermode="outside")

gomb2 = tkinter.Button(top, text="Jelenlegi idő", command=idoButton)
gomb2.place(relx=1, rely=0.0, anchor="ne", bordermode="outside")

jatek = tkinter.Button(top, text="Játék", command=ablaknyitas)
jatek.place(relx=0.5, rely=0.0, anchor="n", bordermode="outside")

kilep = tkinter.Button(top, text="Kilép", command=top.quit)
kilep.place(relx=0.5, rely=1, bordermode="outside", anchor="s")

top.mainloop()
