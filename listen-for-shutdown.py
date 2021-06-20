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

	release = False;
	time.sleep(1)
	if GPIO.input(26):
		print("sudo reboot -h now")
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
		GPIO.output(powerPin, 0);		
		subprocess.call(['reboot', '-h', 'now'], shell=False)
		release = True;
		time.sleep(10);
	GPIO.output(powerPin, 0); # blink once
	time.sleep(0.1);
	GPIO.output(powerPin, 1);
	time.sleep(1)
	if (GPIO.input(26) and (release == False)):
		print("switch to AFSK")
		f = open("/home/pi/CubeSatSim/.mode", "w")
		f.write("a")
		f.close()
		os.system("sudo systemctl stop cubesatsim")
		os.system("sudo systemctl start cubesatsim")
		release = True;
	if (release == False):
		GPIO.output(powerPin, 0); # blink twice
		time.sleep(0.1);
		GPIO.output(powerPin, 1);
		time.sleep(0.1);
		GPIO.output(powerPin, 0);
		time.sleep(0.1);
		GPIO.output(powerPin, 1);	
		time.sleep(1)
	if (GPIO.input(26) and (release == False)):
		print("switch to FSK")
		f = open("/home/pi/CubeSatSim/.mode", "w")
		f.write("f")
		f.close()
		os.system("sudo systemctl stop cubesatsim")
		os.system("sudo systemctl start cubesatsim")
		release = True;
	if (release == False):
		GPIO.output(powerPin, 0); # blink three times
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
	if (GPIO.input(26) and (release == False)):
		print("switch to BPSK")
		f = open("/home/pi/CubeSatSim/.mode", "w")
		f.write("b")
		f.close()
		os.system("sudo systemctl stop cubesatsim")
		os.system("sudo systemctl start cubesatsim")
		release = True;
	if (release == False):
		GPIO.output(powerPin, 0); # blink four times
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
		time.sleep(0.1)
		GPIO.output(powerPin, 0);
		time.sleep(0.1);
		GPIO.output(powerPin, 1);
		time.sleep(1)
	if (GPIO.input(26) and (release == False)):
		print("switch to SSTV")
		f = open("/home/pi/CubeSatSim/.mode", "w")
		f.write("s")
		f.close()
		os.system("sudo systemctl stop cubesatsim")
		os.system("sudo systemctl start cubesatsim")
		release = True;
	if (release == False):
		print("sudo shutdown -h now")
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
		GPIO.output(powerPin, 0); # blink slowly to indicate shutdown
		time.sleep(0.5);
		GPIO.output(powerPin, 1);
		time.sleep(0.5);
		GPIO.output(powerPin, 0);
		time.sleep(0.5);
		GPIO.output(powerPin, 1);
		time.sleep(0.5);
		GPIO.output(powerPin, 0);
		subprocess.call(['shutdown', '-h', 'now'], shell=False)
