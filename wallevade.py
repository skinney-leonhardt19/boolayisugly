import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import sys, tty, termios, signal

import time

RPL.pinMode(17, RPL.INPUT)

while True: 
    if RPL.digitalRead(17) == 1:
        RPL.servoWrite(0, 2000)
        RPL.servoWrite(1, 1000)
        
    if RPL.digitalRead(17) == 0:
        RPL.servoWrite(0, 1000)
        RPL.servoWrite(1, 2000)
