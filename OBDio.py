#!/usr/bin/env python
import serial

class OBDio:
    stopread = 0
    def __init__(portname,baud,to=1):
        self.ser = serial.Serial(port=portname,baudrate=baud,timeout=to);
        
    
    def TestSerialConn(self,):
        ser = serial.Serial("/dev/ttyUSB0", 19200, timeout=1);
        ser.write("AT@1\r")
        x = ser.read();
        s = ser.read(10);
        line = ser.readline();
        ser.close();
        ReadLoop()
        return x,s,line;
    
    def ReadLoop(self,ser):
        #this will be called by the thread and it will read data and when a line is read,
        #it will send the line to the parser to determine where to store it.
        line = ser.read();
        if(line):
            self.callback(line);
    
    def callback(self,line):
        print line;
