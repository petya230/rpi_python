import RPi.GPIO as GPIO
import time

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
	return

def kijelzo1tilt():
    	GPIO.output(kijelzo1, 1)
	return

def kijelzo2ena():
    	GPIO.output(kijelzo2, 0)
	return

def kijelzo2tilt():
    	GPIO.output(kijelzo2, 1)
	return

def kijelzo3ena():
    	GPIO.output(kijelzo3, 0)
	return

def kijelzo3tilt():
    	GPIO.output(kijelzo3, 1)
	return
	
def kijelzo4ena():
    	GPIO.output(kijelzo4, 0)
	return

def kijelzo4tilt():
    	GPIO.output(kijelzo4, 1)
	return

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
	
nulla()
szam = [nulla,egy,ketto,harom,negy,ot,hat,het,nyolc,kilenc]
e = szam[0]
e()

kijelzo1tilt()
kijelzo2tilt()
kijelzo3tilt()
kijelzo4tilt()

for e3 in range(0, 10, 1):
		kijelzo1ena()
		kijelzo2tilt()
		kijelzo3tilt()
		kijelzo4tilt()
		e2 = szam[e3]
		e2()
		kijelzo1tilt()
		for m in range(0, 10, 1):
			kijelzo1tilt()
			kijelzo2ena()
			kijelzo3tilt()
			kijelzo4tilt()
			m2 = szam[m]
			m2()
			kijelzo2tilt()
			for h in range(0, 10, 1):
				kijelzo1tilt()
				kijelzo2tilt()
				kijelzo3ena()
				kijelzo4tilt()
				h2 = szam[h]
				h2()
				kijelzo3tilt()
				for n in range(0, 10, 1):
					kijelzo1tilt()
					kijelzo2tilt()
					kijelzo3tilt()
					kijelzo4ena()
					n2 = szam[n]
					n2()
					kijelzo4tilt()
