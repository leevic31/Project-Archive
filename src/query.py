from collections import defaultdict
import pandas as pd
import database


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
        df = pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)
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


if __name__ == "__main__":
    connection = database.get_db_connection("root", "12345678", "world")
    # printDB(get_DBinfo(connection))
    results = manual_sql_query(
        connection, "select code, name from country where continent ='Asia'")
    print(results)
