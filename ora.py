import RPi.GPIO as GPIO
import time
import datetime

now = datetime.datetime.now()
if now.hour < 10:
		ora = "0" + str(now.hour)
elif now.hour > 10:
	ora = str(now.hour)

if now.minute < 10:
	perc = "0" + str(now.minute)
elif now.minute > 10:
	perc = str(now.minute)


sleep=0.01
i=2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT) # A
GPIO.setup(15, GPIO.OUT) # B
GPIO.setup(17, GPIO.OUT) # C
GPIO.setup(18, GPIO.OUT) # D
GPIO.setup(22, GPIO.OUT) # DP
GPIO.setup(23, GPIO.OUT) # BL
GPIO.setup(27, GPIO.OUT) # LS
GPIO.setup(24, GPIO.OUT) # LS2
GPIO.setup(25, GPIO.OUT) # BL2

kijelzo1 = 23
kijelzo2 = 25
kijelzo3 = 27
kijelzo4 = 24
GPIO.output(kijelzo1, 0)
#kijelzo2
GPIO.output(kijelzo2, 0)
#kijelzo3
GPIO.output(kijelzo3, 0)
#kijelzo4
GPIO.output(kijelzo4, 0)

def kijelzo1ena():
	GPIO.output(kijelzo1, 0)
	return;

def kijelzo1tilt():
	GPIO.output(kijelzo1, 1)
	return;

def kijelzo2ena():
	GPIO.output(kijelzo2, 0)
	return;

def kijelzo2tilt():
	GPIO.output(kijelzo2, 1)
	return;

def kijelzo3ena():
	GPIO.output(kijelzo3, 0)
	return;

def kijelzo3tilt():
	GPIO.output(kijelzo3, 1)
	return;
	
def kijelzo4ena():
	GPIO.output(kijelzo4, 0)
	return;

def kijelzo4tilt():
	GPIO.output(kijelzo4, 1)
	return;

def nulla(): 
# 0
	print("nulla")
	GPIO.output(14, 0)
	GPIO.output(15, 0)
	GPIO.output(17, 0)
	GPIO.output(18, 0)
	GPIO.output(22, 1)
	time.sleep(sleep)
	return;

def egy(): 
# 1
	print("egy")
	GPIO.output(14, 1)
	GPIO.output(15, 0)
	GPIO.output(17, 0)
	GPIO.output(18, 0)
	GPIO.output(22, 1)
	time.sleep(sleep)
	return;

def ketto(): 
# 2
	print("ketto")
	GPIO.output(14, 0)
	GPIO.output(15, 1)
	GPIO.output(17, 0)
	GPIO.output(18, 0)
	GPIO.output(22, 1)
	time.sleep(sleep)
	return;
	
def harom(): 
# 3
	print("harom")
	GPIO.output(14, 1)
	GPIO.output(15, 1)
	GPIO.output(17, 0)
	GPIO.output(18, 0)
	GPIO.output(22, 1)
	time.sleep(sleep)
	return;

def negy(): 
# 4
	print("negy")
	GPIO.output(14, 0)
	GPIO.output(15, 0)
	GPIO.output(17, 1)
	GPIO.output(18, 0)
	GPIO.output(22, 1)
	time.sleep(sleep)
	return;
	
def ot(): 
# 5
	print("ot")
	GPIO.output(14, 1)
	GPIO.output(15, 0)
	GPIO.output(17, 1)
	GPIO.output(18, 0)
	GPIO.output(22, 1)
	time.sleep(sleep)
	return;
	
def hat(): 
# 6
	print("hat")
	GPIO.output(14, 0)
	GPIO.output(15, 1)
	GPIO.output(17, 1)
	GPIO.output(18, 0)
	GPIO.output(22, 1)
	time.sleep(sleep)
	return;
	
def het(): 
# 7
	print("het")
	GPIO.output(14, 1)
	GPIO.output(15, 1)
	GPIO.output(17, 1)
	GPIO.output(18, 0)
	GPIO.output(22, 1)
	time.sleep(sleep)
	return;
	
def nyolc(): 
# 8
	print("nyolc")
	GPIO.output(14, 0)
	GPIO.output(15, 0)
	GPIO.output(17, 0)
	GPIO.output(18, 1)
	GPIO.output(22, 1)
	time.sleep(sleep)
	return;
	
def kilenc(): 
# 9
	print("kilenc")
	GPIO.output(14, 1)
	GPIO.output(15, 0)
	GPIO.output(17, 0)
	GPIO.output(18, 1)
	GPIO.output(22, 1)
	time.sleep(sleep)
	return;

def time1():
	if ora[0] == "0": 
		nulla()
	elif ora[0] == "1":
		egy()
	elif ora[0] == "2": 
		ketto()
	elif ora[0] == "3":
		harom()
	elif ora[0] == "4":
		negy()
	elif ora[0] == "5":
		ot()
	elif ora[0] == "6":
		hat()
	elif ora[0] == "7":
		het()
	elif ora[0] == "8":
		nyolc()
	else:
		kilenc()

def time2():
	if ora[1] == "0": 
		nulla()
	elif ora[1] == "1":
		egy()
	elif ora[1] == "2": 
		ketto()
	elif ora[1] == "3":
		harom()
	elif ora[1] == "4":
		negy()
	elif ora[1] == "5":
		ot()
	elif ora[1] == "6":
		hat()
	elif ora[1] == "7":
		het()
	elif ora[1] == "8":
		nyolc()
	else:
		kilenc()

def time3():
	if perc[0] == "0": 
		nulla()
	elif perc[0] == "1":
		egy()
	elif perc[0] == "2": 
		ketto()
	elif perc[0] == "3":
		harom()
	elif perc[0] == "4":
		negy()
	elif perc[0] == "5":
		ot()
	elif perc[0] == "6":
		hat()
	elif perc[0] == "7":
		het()
	elif perc[0] == "8":
		nyolc()
	else:
		kilenc()

def time4():
	if perc[1] == "0": 
		nulla()
	elif perc[1] == "1":
		egy()
	elif perc[1] == "2": 
		ketto()
	elif perc[1] == "3":
		harom()
	elif perc[1] == "4":
		negy()
	elif perc[1] == "5":
		ot()
	elif perc[1] == "6":
		hat()
	elif perc[1] == "7":
		het()
	elif perc[1] == "8":
		nyolc()
	else:
		kilenc()

nulla()
szam = [nulla,egy,ketto,harom,negy,ot,hat,het,nyolc,kilenc]
e = szam[0]
e()

kijelzo1tilt()
kijelzo2tilt()
kijelzo3tilt()
kijelzo4tilt()

for e3 in range(0, 10, 1): #elso
		kijelzo1ena()
		kijelzo2tilt()
		kijelzo3tilt()
		kijelzo4tilt()
		time1()
		kijelzo1tilt()
		for m in range(0, 10, 1): #masodik
			kijelzo1tilt()
			kijelzo2ena()
			kijelzo3tilt()
			kijelzo4tilt()
			time2()
			kijelzo2tilt()
			for h in range(0, 10, 1): #harmadik
				kijelzo1tilt()
				kijelzo2tilt()
				kijelzo3ena()
				kijelzo4tilt()
				time3()
				kijelzo3tilt()
				for n in range(0, 10, 1): #negyedik
					kijelzo1tilt()
					kijelzo2tilt()
					kijelzo3tilt()
					kijelzo4ena()
					time4()
					kijelzo4tilt()
