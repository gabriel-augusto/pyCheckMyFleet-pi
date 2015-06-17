__author__ = 'gabriel'

import obd
# from obd import utils
import obd_parameters
import sys
from threading import Thread
import time


class ObdReader(Thread, object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ObdReader, cls).__new__(cls, *args)
        return cls._instance

    def __init__(self):
        Thread.__init__(self)
        reload(sys)
        sys.setdefaultencoding('Cp1252')
        self.connection = obd.OBD()
        self.parameters = obd_parameters.ObdParameters()

    def read_obd(self):
        self.parameters.fuel = self.connection.query(obd.commands.FUEL_RATE)
        self.parameters.rpm = self.connection.query(obd.commands.RPM)

    def clear_dtc(self):
        self.connection.query(obd.commands.CLEAR_DTC)

    def run(self):
        while True:
            self.read_obd()
            time.sleep(0.1)
