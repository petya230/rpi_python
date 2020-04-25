# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

#Vizszinterzekelo
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Rele
GPIO.setup(17, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

elso_erzekelo = GPIO.input(18)
masodik_erzekelo = GPIO.input(23)
harmadik_erzekelo = GPIO.input(24)

def automatikus():
    print("automatikus")
    while True:
        file = open('/var/www/html/valasz.txt', 'r')
        sor = (str)(file.readline())
        if (str)(sor) != "automatikus":
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(22, GPIO.HIGH)
            break
        if elso_erzekelo == False:
            print('elso Feltoltve')
            GPIO.output(17, GPIO.HIGH)
            break
        else:
            print('elso Ures')
            GPIO.output(17, GPIO.LOW)
            break
        if masodik_erzekelo == False:
            print('masodik Feltoltve')
            GPIO.output(21, GPIO.HIGH)
            break
        else:
            print('masodik Ures')
            GPIO.output(21, GPIO.LOW)
            break
        if harmadik_erzekelo == False:
            print('harmadik Feltoltve')
            GPIO.output(22, GPIO.HIGH)
            break
        else:
            print('harmadik Ures')
            GPIO.output(22, GPIO.LOW)
            break

def leallitva():
    print("leallitva")
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)

def folyamatos():
    print("folyamatos")
    GPIO.output(17, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)

#file = open('/var/www/html/valasz.txt', 'r')
while (True):
    vissza = [" "," "," "]
    file = open('/var/www/html/valasz.txt', 'r')
    sor = (str)(file.readline())
    ertekek = ""
    kapcsolok = [GPIO.input(18), GPIO.input(23) ,GPIO.input(24)]
    for i in range(len(kapcsolok)):
        if kapcsolok[i] == True:
            vissza[i] = "ures"
        else:
            vissza[i] = "feltoltve"
        ertekek+=vissza[i]
        ertekek+= ";"
    f = open("/var/www/html/vissza.txt", "w")
    f.write(ertekek)
    f.close()

    print("Fájl tartalma: ", sor)
    if (str)(sor) == "automatikus":
        automatikus()
    elif (str)(sor) == "leallitva":
        leallitva()
    elif (str)(sor) == "folyamatos":
        folyamatos()
    else:
        print("NYEH")

    time.sleep(60)