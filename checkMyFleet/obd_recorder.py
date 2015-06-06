__author__ = 'gabriel'

from datetime import datetime
import time
import obd_parameters
import os

class OBDRecorder:
    def __init__(self):
        localtime = time.localtime(time.time())
        filename = "log/car-" + str(localtime[0]) + "-" + str(localtime[1]) + "-" + str(localtime[2]) + "-" + str(
            localtime[3]) + "-" + str(localtime[4]) + "-" + str(localtime[5]) + ".log"
        self.log_file = open(filename, "w", 128)
        self.log_file.write("Time,RPM,MPH,Throttle,Load,Fuel Status\n")
        self.parameters = obd_parameters.ObdParameters()

    def record_data(self):
        localtime = datetime.now()
        current_time = localtime.isoformat()
        log_string = current_time + "," + self.parameters.__str__()
        self.log_file.write(log_string + "\n")