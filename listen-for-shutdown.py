#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
if GPIO.input(12) == False:
	powerPin = 16
else:
	powerPin = 17
GPIO.setwarnings(False)
GPIO.setup(powerPin, GPIO.OUT)
GPIO.output(powerPin, 1);	

while (True):
	time.sleep(1)
	GPIO.wait_for_edge(26, GPIO.FALLING)

	done = False;
	time.sleep(1)
	if GPIO.input(26):
		print("sudo reboot -h now")
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
		GPIO.output(powerPin, 0);		
		subprocess.call(['reboot', '-h', 'now'], shell=False)
	GPIO.output(powerPin, 0);
	time.sleep(0.1);
	GPIO.output(powerPin, 1);
	time.sleep(1)
	if GPIO.input(26):
		print("switch to AFSK")
		f = open("/home/pi/CubeSatSim/.mode", "w")
		f.write("ARG1=a")
		f.close()
		os.system("sudo systemctl stop cubesatsim")
		os.system("sudo systemctl start cubesatsim")
		done = True;
	if (done == False):
		GPIO.output(powerPin, 0);
		time.sleep(0.1);
		GPIO.output(powerPin, 1);
		time.sleep(0.1);
		GPIO.output(powerPin, 0);
		time.sleep(0.1);
		GPIO.output(powerPin, 1);	
		time.sleep(1)
	if (GPIO.input(26) and (done == False)):
		print("switch to FSK")
		f = open("/home/pi/CubeSatSim/.mode", "w")
		f.write("ARG1=f")
		f.close()
		os.system("sudo systemctl stop cubesatsim")
		os.system("sudo systemctl start cubesatsim")
		done = True;
	if (done == False):
		GPIO.output(powerPin, 0);
		time.sleep(0.1);
		GPIO.output(powerPin, 1);
		time.sleep(0.1);
		GPIO.output(powerPin, 0);
		time.sleep(0.1);
		GPIO.output(powerPin, 1);	
		time.sleep(0.1)
		GPIO.output(powerPin, 0);
		time.sleep(0.1);
		GPIO.output(powerPin, 1);	
		time.sleep(1)
	if (GPIO.input(26) and (done == False)):
		print("switch to BPSK")
		f = open("/home/pi/CubeSatSim/.mode", "w")
		f.write("ARG1=b")
		f.close()
		os.system("sudo systemctl stop cubesatsim")
		os.system("sudo systemctl start cubesatsim")
		done = True;
	# time.sleep(1)
	if (done == False):
		print("sudo shutdown -h now")
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
		GPIO.output(powerPin, 0);
		time.sleep(0.5);
		GPIO.output(powerPin, 1);
		time.sleep(0.5);
		GPIO.output(powerPin, 0);
		time.sleep(0.5);
		GPIO.output(powerPin, 1);
		time.sleep(0.5);
		GPIO.output(powerPin, 0);
		subprocess.call(['shutdown', '-h', 'now'], shell=False)
