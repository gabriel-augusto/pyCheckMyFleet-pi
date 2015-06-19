__author__ = 'gabriel'

import obd
import sys
from threading import Thread


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
        obd.Unit.KPA = 'Km/h'
        obd.Unit.LPH = 'L/h'
        self.connection = obd.OBD()
        self.parameters = parameters

    def read_obd(self):
        self.parameters.fuel = self.connection.query(obd.commands.FUEL_RATE)
        if self.parameters.fuel.value is not None:
            self.parameters.fuel.unit = 'L/h'
        self.parameters.rpm = self.connection.query(obd.commands.RPM)
        self.parameters.speed = self.connection.query(obd.commands.SPEED)
        if self.parameters.speed.value is not None:
            self.parameters.fuel.unit = 'Km/h'
        self.parameters.level = self.connection.query(obd.commands.FUEL_LEVEL)
        self.parameters.ethanol = self.connection.query(obd.commands.ETHANOL_PERCENT)

    def clear_dtc(self):
        self.connection.query(obd.commands.CLEAR_DTC)

    def run(self):
        while True:
            self.read_obd()
