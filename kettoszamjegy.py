import RPi.GPIO as GPIO
import time

sleep=0.1
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

#kijelzo1
GPIO.output(27, 0) #datatilt
GPIO.output(23, 1)

#kijelzo2
GPIO.output(24, 0) #datatilt
GPIO.output(25, 0)

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
	GPIO.output(23, 0)
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
	GPIO.output(23, 0)
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
	GPIO.output(23, 1)
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
	
szam = [nulla,egy,ketto,harom,negy,ot,hat,het,nyolc,kilenc]
e = szam[0]
e()

for x in range(0, 10, 1):
	GPIO.output(27, 0)
	GPIO.output(24, 1)
	f = szam[x]
	f()
	GPIO.output(27, 1)
	GPIO.output(24, 0)
	for i in range(1, 10, 1):
		g = szam[i]
		g()
	g = szam[0]
	g()
e = szam[0]
e()