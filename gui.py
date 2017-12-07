#coding: utf-8

import os
temp = os.popen('cat /sys/class/thermal/thermal_zone0/temp').read()
cel = (int(float(temp)) / 1000.0)
#print "%.1f C*" % cel

import datetime

now = datetime.datetime.now()
asd = str(now.hour) + " : " + str(now.minute)
import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def cpu():
   tkMessageBox.showinfo("Fok", cel )

def ido():
   tkMessageBox.showinfo("Idő", asd)

gomb1 = Tkinter.Button(top, text = "CPU hőfok", command = cpu)
gomb1.pack()

gomb2 = Tkinter.Button(top, text = "Jelenlegi idő", command = ido)
gomb2.pack()

kilep = Tkinter.Button(top, text="Kilép", command=top.quit)
kilep.pack()

top.mainloop()
