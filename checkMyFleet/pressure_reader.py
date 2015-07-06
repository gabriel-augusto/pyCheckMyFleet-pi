__author__ = 'gabriel'

from threading import Thread
import serial
import util


class PressureReader(Thread, object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PressureReader, cls).__new__(cls, *args)
        return cls._instance

    def __init__(self, parameters):
        Thread.__init__(self)
        self.parameters = parameters
        self.ser = None
        try:
            self.ser = serial.Serial(port='/dev/ttyAMA0',
                                     baudrate=9600,
                                     parity=serial.PARITY_NONE,
                                     stopbits=serial.STOPBITS_ONE,
                                     bytesize=serial.EIGHTBITS, timeout=1)
        except:
            self.ser = None
            print 'Failed to connect to pressure sensor'

    def read_pressure(self):
        x = self.ser.readline() * 101.5 / 1023
        if util.is_float(x):
            self.parameters.pressure.value = x
            self.parameters.pressure.unit = 'psi'
        else:
            self.parameters.pressure.value = None
            self.parameters.pressure.unit = ''
        print self.parameters.pressure.__str__()

    def run(self):
        while True:
            if self.ser is not None:
                self.read_pressure()
        self.ser.close()
