#/usr/bin/env python
import sys
import time
import serial
import syslog


class LCDWrite:
    global lcd
    lcd=serial.Serial(port="/dev/ttyAMA0",baudrate=9600)
    def configure(self,portdev,baud):
        lcd = serial.Serial(port=portdev,baudrate=baud)
    def write(self,string):
        if lcd.isOpen():
            lcd.write(string)
        else:
            print "Error: LCD Not Open!"
    def newline(self,):
        if lcd.isOpen():
            lcd.write(chr(13))
        else:
            print "Error: LCD Not Open!"
    def clear(self,):
        if lcd.isOpen():
            lcd.write(chr(12))
        else:
            print "Error: LCD Not Open!"
    def backlight(self,state):
        if lcd.isOpen():
            lcd.write(chr(18-state))
        else:
            print "Error: LCD Not Open!"
    def tone(self,):
        if lcd.isOpen():
            lcd.write(chr(220))
        else:
            print "Error: LCD Not Open!"
