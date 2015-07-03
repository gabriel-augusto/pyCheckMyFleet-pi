__author__ = 'gabriel'

import obd
import sys
from threading import Thread
import util


class ObdReader(Thread, object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ObdReader, cls).__new__(cls, *args)
        return cls._instance

    def __init__(self, parameters):
        Thread.__init__(self)
        reload(sys)
        sys.setdefaultencoding('Cp1252')
        obd.debug.console = True
        self.connection = obd.OBD()
        self.parameters = parameters

    def read_obd(self):
        self.parameters.fuel_rate = self.connection.query(obd.commands.FUEL_RATE)
        if self.parameters.fuel_rate.value is not None:
            self.parameters.fuel_rate.unit = 'L/h'

        self.parameters.speed = self.connection.query(obd.commands.SPEED)
        if self.parameters.speed.value is not None:
            self.parameters.speed.unit = 'Km/h'

        self.parameters.rpm = self.connection.query(obd.commands.RPM)
        self.parameters.fuel_level = self.connection.query(obd.commands.FUEL_LEVEL)
        self.parameters.ethanol = self.connection.query(obd.commands.ETHANOL_PERCENT)
        self.parameters.maf = self.connection.query(obd.commands.MAF)

        if util.is_float(self.parameters.speed.value) and util.is_float(self.parameters.maf.value):
            self.parameters.consumption.value = 302.15 * self.parameters.speed.value / self.parameters.maf.value
            self.parameters.consumption.unit = 'Km/L'
        else:
            self.parameters.consumption.value = None
            self.parameters.consumption.unit = ''

    def clear_dtc(self):
        self.connection.query(obd.commands.CLEAR_DTC)

    def run(self):
        while True:
            self.read_obd()
