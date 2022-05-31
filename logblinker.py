#!/usr/bin/env python3
"""
Log Blinker for Adafruit USB tower light w/alarm
"""

import serial
import time
import sys
from collections import defaultdict

serialPort = '/dev/cu.usbserial-143140'  # on mac/linux, it will be a /dev path
baudRate = 9600

NONE   = 0x0
RED    = 0x1
YELLOW = 0x2
GREEN  = 0x4
BUZZER = 0x8
COLORS = RED | YELLOW | GREEN
ALL    = RED | YELLOW | GREEN | BUZZER

ORANGE = RED | YELLOW

ON    = 0x10
OFF   = 0x20
BLINK = 0x40

def sendCommand(serialport, cmd):
	serialport.write(bytes([cmd]))

CODE_COLOR = defaultdict(lambda: GREEN, {
	'3': GREEN | RED,
	'4': ORANGE,
	'5': RED,
})

TYPE_COLOR = defaultdict(lambda: NONE, {
	'png': YELLOW,
	
})

if __name__ == '__main__':
	mSerial = serial.Serial(serialPort, baudRate)
	try:

		for line in sys.stdin:
			print(line)
			field = line.split()
			size3d = float(field[9]) ** (1./3.)
			code = field[8][0]
		
			sendCommand(mSerial, ON | CODE_COLOR[code])
			time.sleep(size3d / 100.)
			sendCommand(mSerial, OFF | ALL)
			time.sleep(0.05)
	
	finally:

		sendCommand(mSerial, OFF | ALL)
		mSerial.close()