from collections import defaultdict
import database


class query():
    info = defaultdict(list)
    db = object()

    def ConnectDB(connection):
        query.db = connection

    def get_DBinfo():
        cursor = query.db.cursor()
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
                    query.info[value].append(column.get("Field"))

    def sql_query(selection, table):
        try:
            cursor = query.db.cursor()
            sql = "Select "
            for item in selection:
                sql += item + " ,"
            sql = sql[:len(sql)-1] + "from " + table
            # execute query
            cursor.execute(sql)
            # print(cursor.description)
            for row in cursor:
                print(row)
        finally:
            query.db.close()

    def printDB():
        for key, values in query.info.items():
            print("Table Name: " + key)
            print("Field Name: ", end="")
            for value in values:
                print(value + ", ", end="")
            print()


if __name__ == "__main__":
    query.ConnectDB(database.get_db_connection("root", "12345678", "world"))
    query.get_DBinfo()
    query.printDB()
    selection = ["code", "name"]
    table = "country"
    query.sql_query(selection, table)
