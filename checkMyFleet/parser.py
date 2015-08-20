__author__ = 'gabriel'

import glob
import os
import time as t
import util
from database import Database

REMOTE_SERVER = "www.google.com"


class LogParameters(dict):
    def __init__(self, placa, pi_serial, date, time, rpm, speed, consumption, autonomy, pressure):
        dict.__init__({})
        self['placa'] = placa
        self['piSerial'] = pi_serial
        self['date'] = date
        self['time'] = time
        self['rpm'] = rpm
        self['speed'] = speed
        self['consumption'] = consumption
        self['autonomy'] = autonomy
        self['pressure'] = pressure

    def __str__(self):
        return (
            "Placa: " + str(self['placa']) + ", piSerial: " + str(self['piSerial']) + ", Date: " + str(
                self['date']) + ", Time: " + str(self['time']) + ", RPM: " + str(self['rpm']) + ", Speed: " + str(
                self['speed']) + ", Consumption: " + str(self['consumption']) + ", Autonomy: " + str(
                self['autonomy']) + ", Pressure: " + str(self['pressure']))


class LogReader:
    def __init__(self):
        self.db = None
        self.log_list = []
        self.text = None
        self.pi_serial = 123456

        try:
            with open('placa/placa.txt') as arc:
                self.placa = arc.readline().strip()
        except IOError as ioerr:
            print("\nIOerr: " + str(ioerr))

    def read_log(self):
        self.db = Database()
        for archive in glob.glob('log/*.log'):
            try:
                with open(archive) as arc:
                    self.text = arc.readlines()
            except IOError as ioerr:
                print("\nIOerr: " + str(ioerr))
            self.text = self.text[0:len(self.text) - 1]

            if self.text:
                self.text.pop(0)
                i = 0
                for eachLine in self.text:
                    if not i % 60:
                        parameters_list = eachLine.strip().split(',')
                        log_parameters = LogParameters(self.placa,
                                                       self.pi_serial,
                                                       parameters_list[0],
                                                       parameters_list[1],
                                                       parameters_list[2],
                                                       parameters_list[3],
                                                       parameters_list[4],
                                                       parameters_list[5],
                                                       parameters_list[6])
                        self.log_list.append(log_parameters)
                        self.db.insert_parameters(log_parameters)
                        print log_parameters.__str__()
                    i += 1
            os.remove(archive)
        self.db.close()

    def __str__(self):
        string = ""
        return string.join([(str(x) + '\n') for x in self.log_list])


if __name__ == "__main__":
    reader = LogReader()
    while True:
        if util.has_internet_connection():
            reader.read_log()
        else:
            t.sleep(3)