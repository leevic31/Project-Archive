import mysql.connector as mysql
import pandas

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

def get_db_connection_with():
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

def insert_data_for(template_name, file_name):
    connection = get_db_connection()
    try:
        connection.autocommit = False

        cursor = connection.cursor()

        sql = ("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` " +
                "WHERE `TABLE_SCHEMA`='{}' AND `TABLE_NAME`='{}'".format(
                config.database, template_name))

        cursor.execute(sql)
        column_names = [column_name[0] for column_name in cursor]

        pyxl.parse_xlsx(file_name, column_names)

        column_names_post = ["`" + column_name + "`" for column_name in column]
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

def get_DBinfo(connection):
    """obtain all field names from each table in the database

    Arguments:
        connection  -- database connection        

    Returns:
        defaultdict -- table name as key, a list of all field names in table as value
    """
    try:
        info = defaultdict(list)
        cursor = connection.cursor()
        # SQL command to list all table
        cursor.execute("SHOW TABLES")
        # iterate all tables
        for tables in cursor.fetchall():
            for table in tables:
                # SQL command to show all column names
                cursor.execute("SHOW COLUMNS FROM " + table)
                for column in cursor.fetchall():
                    # store column names in dictionary with table name as the key
                    info[table].append(column[0])
        return info
    finally:
        connection.close()


def manual_sql_query(connection, command):
    """Run MySQL query and return the result

    Arguments:
        connection  -- database connection
        command {String} -- SQL command

    Returns:
        Dataframe -- contain query result in pandas dataframe format
    """
    try:
        cursor = connection.cursor()
        # execute query
        cursor.execute(command)
        # store the query result in dataframe
        df = pandas.DataFrame(cursor.fetchall())
        return df
    except:
        return None
    finally:
        connection.close()

def printDB(info):
    for key, values in info.items():
        print("Table Name: " + key)
        print("Field Name: ", end="")
        for value in values:
            print(value + ", ", end="")
        print()
