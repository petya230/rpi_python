#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import datetime
import sqlite3 as lite
import sys
import os
import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

#clock
now = datetime.datetime.now()

if now.hour < 10:
		ora = "0" + str(now.hour)
elif now.hour > 10:
	ora = str(now.hour)

if now.minute < 10:
	perc = "0" + str(now.minute)
elif now.minute > 10:
	perc = str(now.minute)
#clock

#TEMP
os.system("sudo modprobe w1-gpio")
os.system("sudo modprobe w1-therm")
devicedir = glob.glob("/sys/bus/w1/devices/28-*")
device = devicedir[0]+"/w1_slave"
f = open (device, 'r')
sensor = f.readlines()
f.close()
crc=sensor[0].split()[-1]
temp=float(sensor[1].split()[-1].strip('t='))
temp_C=(temp/1000.00)
temp_F = ( temp_C * 9.0 / 5.0 ) + 32
#TEMP

#CPUTEMP
cputemp = os.popen('cat /sys/class/thermal/thermal_zone0/temp').read()
cel = (int(float(cputemp)) / 1000.0)
#CPUTEMP

def hofok(n, block_orientation, rotate):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=-90 , rotate=rotate)
    print("Hofok")
    msg = "Hofok: " + str(temp_C) + " C"
    print(msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)


def cpu(n, block_orientation, rotate):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=-90 , rotate=rotate)
    print("CPU Hofok")
    msg = "CPU hofok: " + str(cel) + " C"
    print(msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)

def clock(n, block_orientation, rotate):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=-90 , rotate=rotate)
    print("Ora")
    msg = ora + " : " + perc
    print(msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')

    args = parser.parse_args()


beker = input("Melyiket valasztod? ")
if beker == 0:
        exit()
elif beker == 1:
	hofok(args.cascaded, args.block_orientation, args.rotate)
elif beker == 2:
	cpu(args.cascaded, args.block_orientation, args.rotate)
elif beker == 3:
	clock(args.cascaded, args.block_orientation, args.rotate)
print("nope")

#hofok(args.cascaded, args.block_orientation, args.rotate)
#cpu(args.cascaded, args.block_orientation, args.rotate)
#clock(args.cascaded, args.block_orientation, args.rotate)
