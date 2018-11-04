import sys

import openpyxl
import openpyxl.utils
import mysql.connector

import config

def get_db_connection():

    mydb = mysql.connector.connect(
                host=config.host,
                database=config.database,
                user=config.user,
                password=config.password
                )

    return mydb

def iCare_parse_columns(file_name):
    book = openpyxl.load_workbook(filename = file_name, read_only = True)

    sheet = book.active

    columns = []
    row = 3

    for i in range(1, sheet.max_column + 1):
        cell = "{}{}".format(openpyxl.utils.get_column_letter(i), row)
        columns.append(sheet[cell].value)

    return columns

def iCare_print_columns(file_name):
    book = openpyxl.load_workbook(filename = file_name, read_only = True)

    sheet = book.active

    row = 3

    for i in range(1, sheet.max_column + 1):
    #    cell = "{}{}".format(openpyxl.utils.get_column_letter(i), row)
        print("`{}` varchar(255),".format(openpyxl.utils.get_column_letter(i)))

def add_new_template(name, columnNames, columnTypes):

    connection = get_db_connection()

    try:
        cursor = connection.cursor()
        # Create a new record
        sql = "INSERT INTO `Template`(TemplateName) VALUES (%s)"
        cursor.execute(sql, (name, fields))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()

def parse_row(sheet, column, row):
    vals = []
    row = str(row)
    for col in column:
        print("adding:", col+row)
        if (not sheet[col + row].value):
            vals.append("''")
        else:
            vals.append(sheet[col + row].value)
    return vals

def insert_data_for(template_name, file_name):
    # check whether template_name exists in database

    # get a list of columns the template should have

    # make sure xlsx file has all columns
    connection = get_db_connection()
    try:

        connection.autocommit = False

        cursor = connection.cursor()

        sql = ("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` " +
                "WHERE `TABLE_SCHEMA`='{}' AND `TABLE_NAME`='{}'".format(
                config.database, template_name))

        print("executing:", sql)

        cursor.execute(sql)
        column = [column_name[0] for column_name in cursor]
        print(column)


        book = openpyxl.load_workbook(filename = file_name, read_only = True)
        sheet = book.active

        values = [parse_row(sheet, column, i)
                      for i in range(4, sheet.max_row + 1)]

        column_names = ["`" + column_name + "`" for column_name in column]
        column_formatted = ",".join(column_names)

        tmp = "%s," * len(column_names)
        sql = ("INSERT INTO `{}` ({}) VALUES ".format(template_name, column_formatted) +
               "(" + ("%s," * len(column_names))[:-1] + ")"
              )

        print(sql)

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

def execute_query(query):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()

        cursor.execute(query)
        return cursor
    finally:
        connection.close()

if (__name__ == "__main__"):
    if (len(sys.argv) == 3):
        add_new_template(sys.argv[1], sys.argv[2])
    else:
        print(iCare_print_columns(sys.argv[1]))



#for i in range(1, sheet.max_row + 1):
#	for j in range(1, sheet.max_column + 1):
#		print("{}{}".format(openpyxl.utils.get_column_letter(j), i))

#print(type(book))
#print(type(sheet))

#a1 = sheet['A1']

#print(a1.value)
