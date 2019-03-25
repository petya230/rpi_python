#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
import urllib.request
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

from unidecode import unidecode

global cascaded
cascaded = 8
global block_orientation
block_orientation = -90

# clock
now = datetime.datetime.now()
if now.hour < 10:
    ora = "0" + str(now.hour)
elif now.hour > 10:
    ora = str(now.hour)
if now.minute < 10:
    perc = "0" + str(now.minute)
elif now.minute > 10:
    perc = str(now.minute)
if now.month < 10:
    month = '0' + str(now.month)
elif now.month >= 10:
    month = str(now.month)
day = str(now.day)
####

# Hofok kiolvasasa a szenzorbol
os.system("sudo modprobe w1-gpio")
os.system("sudo modprobe w1-therm")
devicedir = glob.glob("/sys/bus/w1/devices/28-*")
device = devicedir[0]+"/w1_slave"
f = open(device, 'r')
sensor = f.readlines()
f.close()
crc = sensor[0].split()[-1]
temp = float(sensor[1].split()[-1].strip('t='))
temp_C = (temp/1000.00)
temp_F = (temp_C * 9.0 / 5.0) + 32
####

# CPU Hofok kiolvasasa a rendszerbol
cputemp = os.popen('cat /sys/class/thermal/thermal_zone0/temp').read()
cel = (int(float(cputemp)) / 1000.0)
####

def fugvenyek_kivalasztasa(bejovoadat):
    adat = bejovoadat.split(';')
    if (adat[0] == "1"):
        Clock(cascaded, block_orientation, 2)
    if (adat[1] == "1"):
        Cpu(cascaded, block_orientation, 2)
    if (adat[2] == "1"):
        Idojaras(cascaded, block_orientation, 2)
    if (adat[3] == "1"):
        Hofok(cascaded, block_orientation, 2)
    if (adat[4] == "1"):
        Nevnap(cascaded, block_orientation, 2)
    if (adat[5] == "1"):
        Sajatszoveg(cascaded, block_orientation, 2, nem_ascii_karakterek_eltavolitasa(adat[6]))
 
def nem_ascii_karakterek_eltavolitasa(adat):
    for ch in ["[","]","'"]:
       if ch in adat:
         adat=adat.replace( ch,"")
    return unidecode(adat)
	
def nem_ascii_karakterek_eltavolitasa_sajat_szoveg(adat):
    return unidecode(adat)

# nevnap



def nevnap_kinyerese(month, day):
    url = "http://xsak.hu/nevnap/json.php?honap=%s&nap=%s" % (month, day)
    print(url)
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    global mai_nevnap
    mai_nevnap = nem_ascii_karakterek_eltavolitasa((str)(data['nev1']))
    print("Neki van nevnapja: ", mai_nevnap)
####

# weather
API = 'its a secret...'
def idojaras_lekerese(api):
    url = 'http://api.openweathermap.org/data/2.5/weather?&q=Szigethalom,hu&lang=hu&units=metric&appid=%s' % (api)
    print(url)
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    global jelenlegi_idojaras, szelsebesseg
    jelenlegi_idojaras = (data['main']['temp'])
    szelsebesseg = (data['wind']['speed'])
    print("Hofok", jelenlegi_idojaras, "C")
    print("Szelsebesseg", szelsebesseg, "km/h")
####

def Hofok(n, block_orientation, rotate):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=-90, rotate=rotate)
    if ((now.hour + 1) < 9 or (now.hour + 1) > 19):
        device.contrast(1)
        print("Kisebb fényerő")
    print("Hofok")
    msg = "Hofok: " + str(temp_C) + " C"
    print(msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)


def Cpu(n, block_orientation, rotate):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=-90, rotate=rotate)
    if ((now.hour + 1) < 9 or (now.hour + 1) > 19):
        device.contrast(1)
        print("Kisebb fényerő")
    print("CPU Hofok")
    msg = "CPU hofok: " + str(cel) + " C"
    print(msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)


def Clock(n, block_orientation, rotate):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=-90, rotate=rotate)
    if ((now.hour + 1) < 9 or (now.hour + 1) > 19):
        device.contrast(1)
        print("Kisebb fényerő")
    print("Óra")
    msg = ora + " : " + perc + "      " + ora + " : " + perc
    print(msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)


def Idojaras(n, block_orientation, rotate):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=-90, rotate=rotate)
    idojaras_lekerese(API)
    if ((now.hour + 1) < 9 or (now.hour + 1) > 19):
        device.contrast(1)
        print("Kisebb fényerő")
    print("Idojaras")
    msg = "Kinti homerseklet: " + str(jelenlegi_idojaras) + "C Szelsebesseg: " + str(szelsebesseg) + "km/h"
    print(msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)

def Nevnap(n, block_orientation, rotate):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=-90, rotate=rotate)
    nevnap_kinyerese(month, day)
    print("nameday")
    if ((now.hour + 1) < 5 or (now.hour + 1) > 19):
        device.contrast(1)
        print("Kisebb fényerő")
    msg = "Mai nevnap: " + str(mai_nevnap)
    print(msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)

def Sajatszoveg(n, block_orientation, rotate, sajat_szov):
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=-90, rotate=rotate)
    if ((now.hour + 1) < 9 or (now.hour + 1) > 19):
        device.contrast(1)
        print("Kisebb fényerő")
    msg = sajat_szov
	msg = nem_ascii_karakterek_eltavolitasa_sajat_szoveg(msg)
    print(msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    args = parser.parse_args()
