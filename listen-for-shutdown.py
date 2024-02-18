#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time
import os

txPin = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
if GPIO.input(12) == False:
	powerPin = 16
	txPin = 27
	GPIO.setwarnings(False)
	GPIO.setup(txPin, GPIO.OUT)
	GPIO.output(txPin, 0)
else:
	powerPin = 17
GPIO.setwarnings(False)
GPIO.setup(powerPin, GPIO.OUT)
GPIO.output(powerPin, 1)	

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
	time.sleep(1.5)
	if (GPIO.input(26) and (release == False)):
		print("switch to AFSK")
		os.system("/home/pi/CubeSatSim/config -a")
#		f = open("/home/pi/CubeSatSim/.mode", "w")
#		f.write("a")
#		f.close()
#		os.system("sudo sed -i ':a;N;$!ba;s/\nforce_turbo=1//g' /boot/config.txt")
		# os.system("sudo systemctl restart cubesatsim")
		release = True;
	if (release == False):
		GPIO.output(powerPin, 0); # blink twice
		time.sleep(0.1);
		GPIO.output(powerPin, 1);
		time.sleep(0.1);
		GPIO.output(powerPin, 0);
		time.sleep(0.1);
		GPIO.output(powerPin, 1);	
		time.sleep(1.5)
	if (GPIO.input(26) and (release == False)):
		print("switch to FSK")
		os.system("/home/pi/CubeSatSim/config -f")		
#		f = open("/home/pi/CubeSatSim/.mode", "w")
#		f.write("f")
#		f.close()
#		os.system("if ! grep -q force_turbo=1 /boot/config.txt ; then sudo sh -c 'echo force_turbo=1 >> /boot/config.txt'; fi")
		# os.system("sudo systemctl restart cubesatsim")
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
		time.sleep(1.5)
	if (GPIO.input(26) and (release == False)):
		print("switch to BPSK")
		os.system("/home/pi/CubeSatSim/config -b")
#		f = open("/home/pi/CubeSatSim/.mode", "w")
#		f.write("b")
#		f.close()
#		os.system("if ! grep -q force_turbo=1 /boot/config.txt ; then sudo sh -c 'echo force_turbo=1 >> /boot/config.txt'; fi")
		# os.system("sudo systemctl restart cubesatsim")
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
		time.sleep(1.5)
	if (GPIO.input(26) and (release == False)):
		print("switch to SSTV")
		os.system("/home/pi/CubeSatSim/config -s")
#		f = open("/home/pi/CubeSatSim/.mode", "w")
#		f.write("s")
#		f.close()
#		os.system("sudo sed -i ':a;N;$!ba;s/\nforce_turbo=1//g' /boot/config.txt")
		# os.system("sudo systemctl restart cubesatsim")
		release = True;
	if (release == False):
		GPIO.output(powerPin, 0); # blink five times
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
		time.sleep(0.1)
		GPIO.output(powerPin, 0);
		time.sleep(0.1);
		GPIO.output(powerPin, 1);
		time.sleep(1.5)
	if (GPIO.input(26) and (release == False)):
		print("switch to CW")
		os.system("/home/pi/CubeSatSim/config -m")
#		f = open("/home/pi/CubeSatSim/.mode", "w")
#		f.write("m")
#		f.close()
#		os.system("sudo sed -i ':a;N;$!ba;s/\nforce_turbo=1//g' /boot/config.txt")
		# os.system("sudo systemctl restart cubesatsim")
		release = True;
	if (release == False):
		GPIO.output(powerPin, 0); # blink slowly to indicate shutdown
		time.sleep(0.5);
		GPIO.output(powerPin, 1);
		time.sleep(0.5);
		GPIO.output(powerPin, 0);
		time.sleep(0.5);
		GPIO.output(powerPin, 1);
		time.sleep(0.5);
		GPIO.output(powerPin, 0);
		time.sleep(0.5);
		GPIO.output(powerPin, 1);
		time.sleep(1.5);
	if (GPIO.input(26) and (release == False)):
		print("sudo shutdown -h now")
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
		subprocess.call(['shutdown', '-h', 'now'], shell=False)
		release = True;
	if (release == False):
		GPIO.output(powerPin, 0); # blink very slowly to indicate cc toggle
		time.sleep(1.0);
		GPIO.output(powerPin, 1);
		time.sleep(1.0);
		GPIO.output(powerPin, 0);
		time.sleep(1.0);
		GPIO.output(powerPin, 1);
		time.sleep(1.0);
		GPIO.output(powerPin, 0);
		time.sleep(1.0);
		GPIO.output(powerPin, 1);
		time.sleep(1.0);
		GPIO.output(powerPin, 0);	
#	if (GPIO.input(26) and (release == False)):
	else:	
		print("toggle command and control mode")

		try:
			f = open("/home/pi/CubeSatSim/command_control", "r")
			f.close()
			print("command and control will be deactivated")
			os.system('sudo rm /home/pi/CubeSatSim/command_control')
		except:
			print("command and control will be activated")
			os.system('touch /home/pi/CubeSatSim/command_control')
	
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
#		subprocess.call(['reboot', '-h', 'now'], shell=False)
		os.system('sudo systemctl restart cubesatsim')
		release = True;	
#	else:
#		if (txPin != 0):
#			GPIO.setwarnings(False)
#		GPIO.output(txPin, 0)	
#		print("sudo reboot -h now")
#		GPIO.setwarnings(False)
#		GPIO.setup(powerPin, GPIO.OUT)
#		GPIO.output(powerPin, 0);		
#		subprocess.call(['reboot', '-h', 'now'], shell=False)
#		release = True;
#		time.sleep(10);
