import mysql.connector
from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser


def db_connection():
    db_connection = db_configure('config.ini', 'mysql')
    print(db_connection)

    try:
        print('connecting to mysql database')
        connection = MySQLConnection(**db_connection)

        if connection.is_connected():
            print('connected to database established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:
        connection.close()
        print('No longer connected to database.')


def db_configure(file_name, body):
    # parser that reads data from .ini file with initial values
    parser = ConfigParser()
    parser.read(file_name)
    # Emplty dictionary to be populated with elements
    db = {}

    if parser.has_section(body):

        elements = parser.items(body)
        for i in elements:
            db[i[0]] = i[1]

    # A dictionary is returned
    return db



if __name__ == '__main__':
    db_connection()
