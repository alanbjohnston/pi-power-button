#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(26, GPIO.FALLING)

time.sleep(1)
if GPIO.input(26):
	print("sudo shutdown -h now")
	GPIO.setup(10, GPIO.OUT)
	GPIO.output(10, 0);
	time.sleep(1);
	GPIO.output(10, 1);
	time.sleep(1);
	GPIO.output(10, 0);
	subprocess.call(['reboot', '-h', 'now'], shell=False)
time.sleep(1)
if GPIO.input(26):
	print("sudo shutdown -h now")
	subprocess.call(['reboot', '-h', 'now'], shell=False)
else:
	print("sudo reboot now")
	subprocess.call(['shutdown', '-h', 'now'], shell=False)
