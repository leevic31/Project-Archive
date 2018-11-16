import mysql.connector as mysql
import pandas
import pyxl

import config

from collections import defaultdict

def get_db_connection():

    mydb = mysql.connect(
                host=config.host,
                database=config.database,
                user=config.user,
                password=config.password
                )

    return mydb

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
    connection = get_db_connection()

    cursor = connection.cursor()
    # get column names
    sql = ("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` " +
            "WHERE `TABLE_SCHEMA`='{}' AND `TABLE_NAME`='{}'".format(
            config.database, template_name))
    cursor.execute(sql)
    cursor.next()
    column_names = [column_name[0] for column_name in cursor]
    connection.close()
    return column_names

def insert_data_for(template_name, file_name, row_start, row_end):
    connection = get_db_connection()
    try:
        column_names = get_template_attributes(template_name)

        connection.autocommit = False
        cursor = connection.cursor()

        values = pyxl.parse_xlsx(file_name, column_names, row_start, row_end)

        column_names_post = ["`" + column_name + "`"
                                for column_name in column_names]
        column_formatted = ",".join(column_names_post)

        tmp = "%s," * len(column_names_post)
        sql = ("INSERT INTO `{}` ({}) VALUES ".format(template_name,
               column_formatted) + "(" + ("%s," * len(column_names_post))[:-1] +
               ")")

        cursor.execute("START TRANSACTION;")
        for value in values:
            print("Adding:", value)
            cursor.execute(sql, value)

        cursor.execute("COMMIT;")
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

def execute_query_result(query):
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        if (cursor.description):
            values = { i[0]: [] for i in cursor.description }
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

def get_preset_queries():
    conn = get_db_connection()

    # finding number of preset queries
    cursor = conn.cursor()
    quer = "SELECT * FROM Presets"
    cursor.execute(quer)

    results = [row for row in cursor]
    conn.close()

    return results
