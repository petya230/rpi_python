import glob
import time
import os
import datetime
import sqlite3 as lite
import sys

#initialize the device
os.system("sudo modprobe w1-gpio")
os.system("sudo modprobe w1-therm")

#print "DS18B20 - Raspberry Pi"
#find the device
devicedir = glob.glob("/sys/bus/w1/devices/28-*")
device = devicedir[0]+"/w1_slave"

con = lite.connect('homerseklet.db')

while True:
        #open up the file
        f = open (device, 'r')
        sensor = f.readlines()
        f.close()

        #parse results from the file
        crc=sensor[0].split()[-1]
        temp=float(sensor[1].split()[-1].strip('t='))
        temp_C=(temp/1000.000)
        temp_F = ( temp_C * 9.0 / 5.0 ) + 32
        now = datetime.datetime.now()
        dtime = datetime.time(now.hour, now.minute, now.second)

        #output
        if 'YES' in crc:
                print dtime,":\t",temp_C,"*C\t",temp_F,"*F"
                ido = time.strftime("%Y-%m-%d %H:%M:%S")
                with con:
                        cur = con.cursor()
                        cur.execute("INSERT INTO adatok VALUES(?,?)",(ido,temp_C))
        else:
                print dtime,"\tCRC check failed."
                #wait 5 seconds and repeat
        time.sleep(360)
