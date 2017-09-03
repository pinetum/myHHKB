
from serial.tools import list_ports
from time import sleep
import os

targetPort = ""

while targetPort == "":
    ports = list_ports.comports()
    for port_no, description, address in ports:
        if "usbmodem" in port_no and description == "Arduino Leonardo":
            targetPort = port_no
    print("searching port...")
    sleep(1)

cmd = "/Applications/Arduino.app/Contents/Java/hardware/tools/avr/bin/avrdude -C/Applications/Arduino.app/Contents/Java/hardware/tools/avr/etc/avrdude.conf -v -patmega32u4 -cavr109 -P{} -b57600 -D -Uflash:w:hhkb.hex:i"
cmd = cmd.format(targetPort)
print(cmd)
os.system(cmd)
