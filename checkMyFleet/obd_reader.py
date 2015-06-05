__author__ = 'gabriel'

import obd
import obd_parameters


class ObdReader(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ObdReader, cls).__new__(cls, *args)
        return cls._instance

    def __init__(self):
        self.connection = obd.OBD()
        self.parameters = obd_parameters.ObdParameters()
        self.connection.is_connected()
        print self.connection

    def read_obd(self):
        self.parameters.rpm = self.connection.query(obd.commands.RPM)
        self.parameters.speed = self.connection.query(obd.commands.SPEED)
        self.parameters.distance = self.connection.query(obd.commands.DISTANCE_W_MIL)
