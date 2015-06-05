__author__ = 'gabriel'

import MySQLdb


class Database:
    host = '104.131.87.162'
    user = 'root'
    password = '123'
    db = 'test'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()
        self.add_parameters = "INSERT into XXXX (placa, t, rpm, mph, throttle, l, fuel_status) " \
                              "values (%s, %s, %s, %s, %s, %s, %s)"
    '''
    def insert_parameters(self, parameters):
        try:
            self.cursor.execute(
                "INSERT into XXXXX (placa, t, rpm, mph, throttle, l, fuel_status) "
                "values (%s, %s, %s, %s, %s, %s, %s)", (
                    str(parameters['placa']), str(parameters['time']), str(parameters['rpm']), str(parameters['mph']),
                    str(parameters['throttle']), str(parameters['load']), str(parameters['fuel_status'])))
            self.connection.commit()
        except:
            self.connection.rollback()
    '''

    def insert_parameters(self, parameters):
        data = (str(parameters['placa']), str(parameters['time']), str(parameters['rpm']), str(parameters['mph']),
                str(parameters['throttle']), str(parameters['load']), str(parameters['fuel_status']))
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


    def __del__(self):
        self.connection.close()


if __name__ == "__main__":
    db = Database()