__author__ = 'gabriel'

from obd import utils


class ObdParameters(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ObdParameters, cls).__new__(cls, *args)
        return cls._instance

    def __init__(self):
        self.rpm = utils.Response()
        self.speed = utils.Response()
        self.throttle = utils.Response()
        self.load = utils.Response()
        self.fuel_rate = utils.Response()
        self.distance = utils.Response()
        self.economy = utils.Response()
        self.ethanol = utils.Response()
        self.fuel_level = utils.Response()

    def __str__(self):
        return str(self.rpm.value) + "," + str(self.speed.value) + "," + str(self.fuel_rate.value) + "," + str(
            self.fuel_level.value) + "," + str(self.ethanol.value)