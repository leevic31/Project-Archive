import mysql.connector as mysql
import pandas
import pyxl
import config
from collections import defaultdict

from collections import defaultdict


def get_db_connection():
    '''() -> connection
    get and return the database connection
    '''

    mydb = mysql.connect(
        host=config.host,
        database=config.database,
        user=config.user,
        password=config.password
    )

    return mydb

def add_user(agency_name, agency_address, user_name,
        user_email, user_password):

    connection = get_db_connection()
    connection.autocommit = True
    with connection:
        try:
            my_cursor = connection.cursor()
            my_cursor.execute("INSERT INTO User (AgencyName, AgencyAddress, UserEmail, UserPassword, UserName, UserType) VALUES (?, ?, ?, ?, ?, ?)",
                (agency_name, agency_address,
                 user_email, user_password, user_name))

        except Error as error:
            print(error)

        finally:
            connection.close()

def get_user_type(useremail, password) -> str:

    connection = get_db_connection()
    connection.autocommit = True
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT UserType FROM User WHERE UserEmail = %s " +
                          "AND UserPassword = %s", (useremail, password))
        row = cursor.fetchone()
        if (row is None):
            return None
        else:
            return row[0]

    finally:
        connection.close()

def get_user_password(useremail):
    connection = get_db_connection()
    connection.autocommit = True
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT UserPassword FROM User WHERE UserEmail = %s " 
                       , (useremail))
        row = cursor.fetchone()
        if (row is None):
            return None
        else:
            return row[0]

    finally:
        connection.close()

def get_db_connection_with(username, password, database):
    '''coonect to the database server

    Args:
        username (string): username
        password (string): password
        database (string): database schemas

    Returns:
        object: database
    '''

    connection = mysql.connect(host='localhost',
                               database=database,
                               user=username,
                               password=password
                               )
    return connection


def get_template_attributes(template_name):
    '''(str) -> list of str
    Given the name of a Template name, return the column names associated
    to that template in the database

    '''
    connection = get_db_connection()

    cursor = connection.cursor()
    # get column names
    sql = ("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` " +
           "WHERE `TABLE_SCHEMA`='{}' AND `TABLE_NAME`='{}'".format(
               config.database, template_name))
    cursor.execute(sql)

    # do not return non template attributes
    cursor.next()


    column_names = [column_name[0] for column_name in cursor]
    connection.close()
    return column_names

def insert_iCare_data(template_name, file_name):
    '''(str, str, int, int) -> None
    Insert template values into the database for the specific template
    '''
    connection = get_db_connection()
    try:
        # get the column names for this Template
        column_names = get_template_attributes(template_name)

        connection.autocommit = False
        cursor = connection.cursor()

        # get all the row values in the xlsx file
        values = pyxl.parse_xlsx(file_name, column_names)

        column_names_post = ["`" + column_name + "`"
                             for column_name in column_names]
        column_formatted = ",".join(column_names_post)

        tmp = "%s," * len(column_names_post)
        sql = ("INSERT INTO `{}` ({}) VALUES ".format(template_name,
                                                      column_formatted) + "(" + ("%s," * len(column_names_post))[:-1] +
               ")")

        cursor.execute("START TRANSACTION")
        for value in values:
            cursor.execute(sql, value)

        cursor.commit()
        print("Data has been successfully added to the database")

    finally:
        connection.close()


def get_iCare_template_names():
    try:
        connection = get_db_connection()

        cursor = connection.cursor()
        # Create a new record
        sql = "SELECT TemplateName from `Template`"
        cursor.execute(sql)
        iCare_names = [template_name[0] for template_name in cursor]

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
        connection.close()
        return iCare_names
    except:
        print("Failed to connect to database")
        return []

def get_preset_queries():
    conn = get_db_connection()

    # finding number of preset queries
    cursor = conn.cursor()
    quer = "SELECT * FROM Presets"
    cursor.execute(quer)

    results = [row for row in cursor]
    conn.close()

    return results

def execute_query_result(query):
    connection = get_db_connection()
    connection.autocommit = True
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        if (cursor.description):
            values = {i[0]: [] for i in cursor.description}
            for row in cursor:
                for value in row:
                    values[value].append(row[value])
            return values
    finally:
        connection.close()


def query_to_dataframe(query):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        df = pandas.DataFrame(cursor.fetchall())
        return df
    finally:
        connection.close()
