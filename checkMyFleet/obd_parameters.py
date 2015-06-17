__author__ = 'gabriel'

from obd import utils


class ObdParameters(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ObdParameters, cls).__new__(cls, *args)
        return cls._instance

    def __init__(self):
        utils.Unit.KPA = 'Km/h'
        self.rpm = utils.Response()
        self.speed = utils.Response()
        self.throttle = utils.Response()
        self.load = utils.Response()
        self.fuel = utils.Response()
        self.distance = utils.Response()
        self.econometer = utils.Response()

    def __str__(self):
        return str(self.rpm.value) + "," + str(self.speed.value) + "," + str(self.throttle.value) + "," + str(
            self.load.value) + "," + str(self.fuel.value) + "," + str(self.distance.value) + "," + str(
            self.econometer.value)