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
        curpath = os.path.abspath(os.curdir)
        self.path = os.path.join(curpath, filename)

        mode = 'a' if os.path.exists(self.path) else 'w'
        with open(self.path, mode) as f:
            f.write("Time,RPM,MPH,Throttle,Load,Fuel Status, Distance\n")

        self.parameters = obd_parameters.ObdParameters()

    def record_data(self):
        localtime = datetime.now()
        current_time = localtime.isoformat()
        log_string = current_time + "," + self.parameters.__str__

        mode = 'a' if os.path.exists(self.path) else 'w'
        with open(self.path, mode) as f:
            f.write(log_string + "\n")
