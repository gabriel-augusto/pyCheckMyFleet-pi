__author__ = 'gabriel'


class ObdParameters(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ObdParameters, cls).__new__(cls, *args)
        return cls._instance

    def __init__(self):
        self.rpm = 0
        self.speed = 0
        self.distance = 0