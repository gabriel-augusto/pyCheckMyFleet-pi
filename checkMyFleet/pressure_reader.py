__author__ = 'gabriel'

from threading import Thread
import serial
import util
import time


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
        x = self.ser.readline().strip()
        if util.is_float(x):
            x = float(x) * 101.5 / 1023
            x = round(x, 2)
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
            time.sleep(0.5)
        self.ser.close()
