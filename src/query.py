from collections import defaultdict
import pandas as pd


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
    cursor = connection.cursor()
    # execute query
    cursor.execute(command)
    # store the query result in dataframe
    df = pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)
    return df


