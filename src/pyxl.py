import sys

import openpyxl
import openpyxl.utils
import mysql.connector

def get_db_connection():
    mydb = mysql.connector.connect(
                host='localhost',
                database='c43',
                user='shana',
                password='zhaoji97'
                )

    return mydb

def add_new_template(name, file_name):
    book = openpyxl.load_workbook(filename=file_name,
                read_only=True)

    sheet = book.active

    row = 3
    fields = ""
    for i in range(1, sheet.max_column + 1):
        cell = "{}{}".format(openpyxl.utils.get_column_letter(i), row)
        fields += sheet[cell].value + ","
        print("{}: {}".format(cell, sheet[cell].value))
    fields = fields[:-1]

    connection = get_db_connection()

    try:
        cursor = connection.cursor()
        # Create a new record
        sql = "INSERT INTO `Template`(`template_name`, `template_fields`) VALUES (%s, %s)"
        cursor.execute(sql, (name, fields))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()

def insert_data_for(template_name, file_name):
    # check whether template_name exists in database

    # get a list of columns the template should have

    # make sure xlsx file has all columns
    pass

def get_iCare_template_names():
    connection = get_db_connection()
    iCare_names = []

    try:
        cursor = connection.cursor()
        # Create a new record
        sql = "SELECT template_name from `Template`"
        cursor.execute(sql)
        iCare_names = [template_name[0] for template_name in cursor]

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()

    return iCare_names

if (__name__ == "__main__"):
    if (len(sys.argv) == 3):
        add_new_template(sys.argv[1], sys.argv[2])
    else:
        print(get_iCare_template_names())



#for i in range(1, sheet.max_row + 1):
#	for j in range(1, sheet.max_column + 1):
#		print("{}{}".format(openpyxl.utils.get_column_letter(j), i))

#print(type(book))
#print(type(sheet))

#a1 = sheet['A1']

#print(a1.value)
