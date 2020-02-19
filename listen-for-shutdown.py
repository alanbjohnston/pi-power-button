#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(26, GPIO.FALLING)

time.sleep(1)
if GPIO.input(26):
	print("sudo reboot -h now")
	subprocess.call(['reboot', '-h', 'now'], shell=False)
time.sleep(1)
if GPIO.input(26):
	print("sudo reboot -h now")
	subprocess.call(['reboot', '-h', 'now'], shell=False)
else:
	print("sudo shutdown -h now")
	GPIO.setwarnings(False)
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, 0);
	time.sleep(1);
	GPIO.output(17, 1);
	time.sleep(1);
	GPIO.output(17, 0);
	subprocess.call(['shutdown', '-h', 'now'], shell=False)
