__author__ = 'gabriel'

from datetime import datetime
import time
import os
from threading import Thread


class OBDRecorder(Thread):
    def __init__(self, parameters):
        Thread.__init__(self)
        localtime = time.localtime(time.time())
        filename = "log/car-" + str(localtime[0]) + "-" + str(localtime[1]) + "-" + str(localtime[2]) + "-" + str(
            localtime[3]) + "-" + str(localtime[4]) + "-" + str(localtime[5]) + ".log"
        current_path = os.path.abspath(os.curdir)
        self.path = os.path.join(current_path, filename)
        self.parameters = parameters

    def record_data(self):
        localtime = datetime.now()
        current_time = localtime.isoformat().split('T')
        log_string = current_time[0] + "," + current_time[1] + "," + self.parameters.__str__()

        if os.path.exists(self.path):
            with open(self.path, 'a') as f:
                f.write(log_string + "\n")
        else:
            with open(self.path, 'w') as f:
                f.write("Date,Time,RPM,Speed,Consumption,Autonomy,Pressure\n")

    def run(self):
        while True:
            self.record_data()
            time.sleep(1)