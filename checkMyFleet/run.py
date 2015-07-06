__author__ = 'gabriel'

import subprocess
import bluetooth
import os
from obd_reader import ObdReader
from obd_recorder import OBDRecorder
from gui import Render
from obd_parameters import ObdParameters
from pressure_reader import PressureReader
# import time


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
        # subprocess.Popen(["sudo", "rfcomm", "connect", "4"])
        # time.sleep(3)
        os.system("sudo rfcomm bind all")
        # subprocess.Popen(["sudo", "rfcomm", "connect", "0", target_address, "1"])
        print "Connected!!!\n\n"
        break
    else:
        print "could not find target bluetooth device nearby"

subprocess.Popen(["python", "parser.py"])
# subprocess.Popen(["python", "wifi_connect.py"])

parameters = ObdParameters()

obd_reader = ObdReader(parameters)
obd_reader.setName('OBD Reader')

pressure_reader = PressureReader(parameters)
pressure_reader.setName('Pressure Reader')

recorder = OBDRecorder(parameters)
recorder.setName('Recorder')

render = Render(parameters)
render.setName('Render')

obd_reader.start()
pressure_reader.start()
recorder.start()
render.start()

obd_reader.join()
pressure_reader.join()
recorder.join()
render.join()
