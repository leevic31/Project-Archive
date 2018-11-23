'''
Unused file; kept for future reference
'''

import mysql.connector
from mysql.connector import MySQLConnection, Error
import db_config


def db_connection():
    mydb = mysql.connector.connect(host=db_config.host, database=db_config.database, user=db_config.user, password=db_config.password)
    return mydb

def add_agency():
    connection = db_connection()
    with connection:
        try:
            my_cursor = connection.cursor()
            my_cursor.execute("USE testdb")
            my_cursor.execute("INSERT INTO Agency(AgencyName, AgencyAddress, NumberOfEmployees, iCARETemplateChoice)"
                              "VALUES('%s, %s, %s, %s')" % (''.join(self.))
            )

        except Error as error:
            print(error)

        finally:
            connection.close()



if __name__ == '__main__':
    db_connection()
