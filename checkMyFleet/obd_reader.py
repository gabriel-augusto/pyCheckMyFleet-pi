__author__ = 'gabriel'

import obd
from obd import utils
import obd_parameters
import sys


class ObdReader(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ObdReader, cls).__new__(cls, *args)
        return cls._instance

    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('Cp1252')
        self.connection = obd.OBD()
        self.parameters = obd_parameters.ObdParameters()

    def read_obd(self):
        self.parameters.rpm = self.connection.query(obd.commands.RPM)
        self.parameters.speed = self.connection.query(obd.commands.SPEED)
        self.parameters.throttle = self.connection.query(obd.commands.THROTTLE_POS)
        self.parameters.load = self.connection.query(obd.commands.ENGINE_LOAD)
        self.parameters.fuel_status = self.connection.query(obd.commands.FUEL_STATUS)
        self.parameters.distance = self.connection.query(obd.commands.DISTANCE_SINCE_DTC_CLEAR)
        if self.parameters.throttle.value is not None:
            self.parameters.econometer.value = 100 - self.parameters.throttle.value
            self.parameters.econometer.unit = utils.Unit.PERCENT
        else:
            self.parameters.econometer.value = None
            self.parameters.econometer.unit = utils.Unit.NONE
