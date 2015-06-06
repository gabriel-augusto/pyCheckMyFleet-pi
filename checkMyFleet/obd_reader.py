__author__ = 'gabriel'

import obd
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
        self.parameters.rpm = self.connection.query(obd.commands.RPM).value
        self.parameters.speed = self.connection.query(obd.commands.SPEED).value
        # self.parameters.distance = self.connection.query(obd.commands.DISTANCE_W_MIL).vallue
