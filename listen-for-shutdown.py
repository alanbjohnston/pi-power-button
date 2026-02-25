#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import time
import os
from time import sleep
from os import system

def output(pin, value):
	command = "gpio -g write " + str(pin) + " " + str(value)
	system(command)
	print(command)

def input(pin):
	# command = "gpio -g read " + str(pin)
	query = ["gpio", "-g", "read", str(pin)] # Read GPIO pin
	try:
		result = subprocess.run(query, capture_output=True, text=True, check=True)
		print(f"Command run was: {query}")
		print("Sucess!")
		print(f"Output of the command (stdout): {result.stdout}")
		return int(result.stdout)
	except subprocess.CalledProcessError as e:
		print(f"Command failed with return code: {e.returncode}")
		print(f"Command run was: {e.cmd}")
		print(f"Output of the command (stdout): {e.stdout}")
		print(f"Error output of the command (stderr): {e.stderr}")
		return -1

def setup(pin, config):
	if config == "in" or config == "out" or config == "up" or config == "down":
		command = "gpio -g mode " + str(pin) + " " + config
		system(command)
		print(command)
	else:
		print(f"Unknown GPIO setup configuration: {config}")

def blink(times):
	powerPin = 16
	for i in range(times):
		system("gpio -g write " + str(powerPin) + " 0") # blink two times
		sleep(0.1)
		system("gpio -g write " + str(powerPin) + " 1")
		sleep(0.1)
	sleep(0.65)	

#def blink(times):
#	blink_time = 0.1
#	powerPin = 16
#	for i in range(times):	# blink times
#		GPIO.output(powerPin, 0) 
#		sleep(blink_time)
#		GPIO.output(powerPin, 1)
#		sleep(blink_time)
#	sleep(0.65)

def change_mode():
	buttonPin = 26
	powerPin = 16
	txPin = 27
	sleep(0.75)
	if GPIO.input(buttonPin):
		print("sudo reboot -h now")
		os.system("echo 'reboot due to push button!' | wall")
#		GPIO.setwarnings(False)
#		GPIO.setup(powerPin, GPIO.OUT)
#		GPIO.output(powerPin, 0)	
		output(powerPin, 0)
		subprocess.call(['reboot', '-h', 'now'], shell=False)
		return
	blink(1)
	if GPIO.input(buttonPin):
		print("switch to AFSK")
		os.system("echo 'switch to AFSK due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -a")
		return
	blink(2)	
	if GPIO.input(buttonPin):
		print("switch to FSK")
		os.system("echo 'switch to FSK due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -f")		
		return
	blink(3)
	if GPIO.input(buttonPin):
		print("switch to BPSK")
		os.system("echo 'switch to BPSK due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -b")
		return
	blink(4)
	if GPIO.input(buttonPin):
		print("switch to SSTV")
		os.system("echo 'switch to SSTV due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -s")
		return
	blink(5)
	if GPIO.input(buttonPin):
		print("switch to CW")
		os.system("echo 'switch to CW due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -m")
		return
	blink(6)
	if GPIO.input(buttonPin):
		print("switch to Repeater")
		os.system("echo 'switch to Repeater due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -e")
		return
	blink(7)
	if GPIO.input(buttonPin):
		print("switch to FunCube")
		os.system("echo 'switch to FunCube due to push button!' | wall")
		os.system("/home/pi/CubeSatSim/config -j")
		return
	for i in range(3):	# blink 3 times slowly
#		GPIO.output(powerPin, 0) 
		output(powerPin, 0)
		sleep(0.35)
#		GPIO.output(powerPin, 1)
		output(powerPin, 1)
		sleep(0.35)
	sleep(0.65)
	if GPIO.input(buttonPin):
		print("sudo shutdown -h now")
		os.system("echo 'shutdown due to push button!' | wall")
		GPIO.setwarnings(False)
		GPIO.setup(powerPin, GPIO.OUT)
		subprocess.call(['shutdown', '-h', 'now'], shell=False)
		return
	for i in range(3):	# blink two times even more slowly
#		GPIO.output(powerPin, 0)
		output(powerPin, 0)
		sleep(0.7)
#		GPIO.output(powerPin, 1)
		output(powerPin, 1)
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

powerPin = 16
txPin = 27
buttonPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(txPin, GPIO.OUT)
#GPIO.output(txPin, 0)
output(txPin, 0)
#GPIO.setup(powerPin, GPIO.OUT)
#GPIO.output(powerPin, 1)
output(powerPin, 1)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while (True):
	sleep(1)
	GPIO.wait_for_edge(buttonPin, GPIO.FALLING)
	change_mode()
	sleep(5)
