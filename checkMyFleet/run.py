__author__ = 'gabriel'

import subprocess
import bluetooth
import os
import time

target_name = "OBDII"
target_address = None

while True:

    nearby_devices = bluetooth.discover_devices()

    print(nearby_devices)

    for device in nearby_devices:
        if target_name == bluetooth.lookup_name(device):
            target_address = device
            break

    if target_address is not None:
        print "found target bluetooth device with address ", target_address
        # os.system("sudo rfcomm bind all")
        subprocess.Popen(["sudo", "rfcomm", "connect", "0", target_address, "1"])
        print "Connected!!!\n\n"
        break
    else:
        print "could not find target bluetooth device nearby"

subprocess.Popen(["sudo", "python", "gui.py"])
