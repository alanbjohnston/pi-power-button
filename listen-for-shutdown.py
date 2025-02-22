#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import time
import os
from time import sleep

def blink(times):
	blink_time = 0.07
	powerPin = 16
	for i in range(times):	# blink times
		GPIO.output(powerPin, 0) 
		sleep(blink_time)
		GPIO.output(powerPin, 1)
		sleep(blink_time)
	sleep(blink_time * 15 - blink_time)

def change_mode():
	push_button = 26
	powerPin = 16
	txPin = 27

	if GPIO.input(push_button):
		print("sudo reboot -h now")
		os.system("echo 'reboot due to push button!' | wall")
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
		GPIO.output(powerPin, 0);		
		subprocess.call(['reboot', '-h', 'now'], shell=False)
		return
	blink(1)
	if GPIO.input(push_button):
		print("switch to AFSK")
		os.system("echo 'switch to AFSK due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -a")
		return
	blink(2)	
	if GPIO.input(push_button):
		print("switch to FSK")
		os.system("echo 'switch to FSK due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -f")		
		return
	blink(3)
	if GPIO.input(push_button):
		print("switch to BPSK")
		os.system("echo 'switch to BPSK due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -b")
		return
	blink(4)
	if GPIO.input(push_button):
		print("switch to SSTV")
		os.system("echo 'switch to SSTV due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -s")
		return
	blink(5)
	if GPIO.input(push_button):
		print("switch to CW")
		os.system("echo 'switch to CW due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -m")
		return
	blink(6)
	if GPIO.input(push_button):
		print("switch to Repeater")
		os.system("echo 'switch to Repeater due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -e")
		return
	blink(7)
	if GPIO.input(push_button):
		print("switch to FunCube")
		os.system("echo 'switch to FunCube due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -j")
		return
	for i in range(3):	# blink 3 times slowly
		GPIO.output(powerPin, 0) 
		sleep(0.35)
		GPIO.output(powerPin, 1)
		sleep(0.35)
	sleep(0.65)
	if (GPIO.input(push_button):
		print("sudo shutdown -h now")
		os.system("echo 'shutdown due to push button!' | wall")
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
		subprocess.call(['shutdown', '-h', 'now'], shell=False)
		return
	for i in range(3):	# blink two times even more slowly
		GPIO.output(powerPin, 0) 
		sleep(0.7)
		GPIO.output(powerPin, 1)
		sleep(0.7)
	sleep(0.7)
	print("toggle command and control mode")
	try:
		f = open("/home/pi/CubeSatSim/command_control", "r")
		f.close()
		print("command and control will be deactivated")
		os.system('sudo rm /home/pi/CubeSatSim/command_control')
		os.system("echo 'command and control deactivated by push button!' | wall")
		os.system('sudo systemctl restart command')
	except:
		print("command and control will be activated")
		os.system('touch /home/pi/CubeSatSim/command_control')
		os.system("echo 'command and control activated by push button!' | wall")
		os.system('sudo systemctl restart command')
	sleep(1)
	
#txPin = 0
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#if GPIO.input(12) == False:
#	powerPin = 16
#	txPin = 27
#	GPIO.setwarnings(False)
#	GPIO.setup(txPin, GPIO.OUT)
#	GPIO.output(txPin, 0)
#else:
#	powerPin = 17

	
powerPin = 16
txPin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(txPin, GPIO.OUT)
GPIO.output(txPin, 0)
GPIO.setwarnings(False)
GPIO.setup(powerPin, GPIO.OUT)
GPIO.output(powerPin, 1)

while (True):
	time.sleep(1)
	GPIO.wait_for_edge(26, GPIO.FALLING)
	change_mode()
