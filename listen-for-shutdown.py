#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
if GPIO.input(12) == False:
	powerPin = 16
else:
	powerPin = 17
	
while (True):	
	GPIO.wait_for_edge(26, GPIO.FALLING)

	done = False;
	time.sleep(1)
	if GPIO.input(26):
		print("sudo reboot -h now")
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
		GPIO.output(powerPin, 0);		
		subprocess.call(['reboot', '-h', 'now'], shell=False)
	time.sleep(1)
	if GPIO.input(26):
		print("sudo reboot -h now")
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
		GPIO.output(powerPin, 0);
		subprocess.call(['reboot', '-h', 'now'], shell=False)
	time.sleep(1)
	GPIO.setwarnings(False)
	GPIO.setup(powerPin, GPIO.OUT)
	GPIO.output(powerPin, 0);
	time.sleep(0.1);
	GPIO.output(powerPin, 1);
	if GPIO.input(26):
		print("switch to AFSK")
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
		done = True;
	time.sleep(1)
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
