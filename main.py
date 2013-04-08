#!/usr/bin/env python
import serial
from OBDio import OBDio
from LCDio import LCDWrite
OBDio = OBDio("/dev/ttyUSB0",115200)
lcd = LCDWrite();
def main():
    print OBDio.TestSerialConn();
    lcd.configure("/dev/ttyAMA0",19200);
    lcd.write("test");
    return;


main();
