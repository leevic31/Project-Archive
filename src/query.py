from collections import defaultdict
import database


class query():

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
            results = cursor.fetchall()
            # iterate all tables
            for result in results:
                for key, value in result.items():
                    # SQL command to show all column names
                    cursor.execute("SHOW COLUMNS FROM " + value)
                    columns = cursor.fetchall()
                    for column in columns:
                        # store column names in dictionary with table name as the key
                        info[value].append(column.get("Field"))
            return info
        finally:
            connection.close()

    def manual_sql_query(connection, command):
        """Run MySQL query and return the result

        Arguments:
            connection  -- database connection
            command {String} -- SQL command

        Returns:
            Dictionary in List -- the list contains all records from query in dictionary format, while column as key and data as vaule in the dictionary 
        """
        try:
            cursor = connection.cursor()
            # execute query
            cursor.execute(command)
            data = cursor.fetchall()
            return data
        finally:
            connection.close()

    def printDB(info):
        for key, values in info.items():
            print("Table Name: " + key)
            print("Field Name: ", end="")
            for value in values:
                print(value + ", ", end="")
            print()

    def printData(info):
        for item in info:
            print(item)


if __name__ == "__main__":
    connection = database.get_db_connection("root", "12345678", "world")
    # query.printDB(query.get_DBinfo(connection))
    results = query.manual_sql_query(
        connection, "select code, name from country where continent ='Asia'")
