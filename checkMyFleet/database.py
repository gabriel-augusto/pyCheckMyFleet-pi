__author__ = 'gabriel'

import MySQLdb


class Database:
    host = '104.131.87.162'
    user = 'checkmyfleet'
    password = 'macaco'
    db = 'checkmyfleet'
    table = 'Measurement'

    def __init__(self):
        self.add_parameters = "INSERT into Measurement (vehiclePlate, piSerial, measurementDate, measurementTime, rpm, kph, fuelRate, fuelLevel, ethanolPercent) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    '''
    def connect(self):
        try:
            self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
            self.cursor = self.connection.cursor()
        except:
            pass
    '''

    '''
    def insert_parameters(self, parameters):
        try:
            self.cursor.execute(
                "INSERT into Measurement (placa, t, rpm, mph, throttle, l, fuel_status) "
                "values (%s, %s, %s, %s, %s, %s, %s)", (
                    str(parameters['placa']), str(parameters['time']), str(parameters['rpm']), str(parameters['mph']),
                    str(parameters['throttle']), str(parameters['load']), str(parameters['fuel_status'])))
            self.connection.commit()
        except:
            self.connection.rollback()
    '''

    def insert_parameters(self, parameters):
        data = (str(parameters['placa']),
                str(parameters['piSerial']),
                str(parameters['date']),
                str(parameters['time']),
                str(parameters['rpm']),
                str(parameters['speed']),
                str(parameters['consumption']),
                str(parameters['autonomy']),
                str(parameters['pressure']))
        self.insert(self.add_parameters, data)

    def insert(self, query, data):
        try:
            self.cursor.execute(query, data)
            self.connection.commit()
        except:
            self.connection.rollback()

    def query(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)

        return cursor.fetchall()

    def insert_simulation(self):
        data = (2, 20, 'teste_lindo')
        self.insert(self.add_parameters, data)

    def close(self):
        if self.connection is not None:
            self.connection.close()


if __name__ == "__main__":
    db = Database()