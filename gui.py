#coding: utf-8

import os
temp = os.popen('cat /sys/class/thermal/thermal_zone0/temp').read()
cel = (int(float(temp)) / 1000.0)
#print "%.1f C*" % cel

import datetime

now = datetime.datetime.now()

import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def cpu():
   tkMessageBox.showinfo("Cpu hőfok: % C*", cel )

def ido():
   tkMessageBox.showinfo("Idő: %s:%s" % (now.hour, now.minute))

gomb1 = Tkinter.Button(top, text = "CPU hőfok", command = cpu)
gomb1.pack()

gomb2 = Tkinter.Button(top, text = "Jelenlegi idő", command = ido)
gomb2.pack()

kilep = Tkinter.Button(top, text="Kilép", command=top.quit)
kilep.pack()

top.mainloop()
