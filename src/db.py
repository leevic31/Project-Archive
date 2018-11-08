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