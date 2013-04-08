#!/usr/bin/env python
import serial
from OBDio import OBDio
OBDio = OBDio("/dev/ttyUSB0",115200)

def main():
    print OBDio.TestSerialConn()
    return


main();
