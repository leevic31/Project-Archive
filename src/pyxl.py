import sys

import openpyxl
import openpyxl.utils
import pymysql.cursors

def add_new_template(name, file_name):
    book = openpyxl.load_workbook(filename=file_name,
                read_only=True)

    sheet = book.active

    row = 2
    fields = ""
    for i in range(1, sheet.max_column + 1):
        cell = "{}{}".format(openpyxl.utils.get_column_letter(i), row)
        fields += sheet[cell].value + ","
        print("{}: {}".format(cell, sheet[cell].value))
    fields = fields[:-1]

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='shana',
                                 password='zhaoji97',
                                 db='c43',
                             #    charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
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



if (__name__ == "__main__"):
    if (sys.argc != 2):
        print("usage: {} name file", sys.argv[0])
        return 1

    add_new_template(argv[1], argv[2])


#for i in range(1, sheet.max_row + 1):
#	for j in range(1, sheet.max_column + 1):
#		print("{}{}".format(openpyxl.utils.get_column_letter(j), i))

#print(type(book))
#print(type(sheet))

#a1 = sheet['A1']

#print(a1.value)
