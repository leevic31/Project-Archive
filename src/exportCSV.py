import database
import query
from os import path
import pandas as pd

class ExportCSV:
    def export(self, file_path, query_text):
        conn = database.get_db_connection()
        dataframe = query.manual_sql_query(conn, query_text)
        dataframe.to_csv(file_path, index=False)


def exportCSV(file_path, query_result):
    """Export the query result into CSV file

    Arguments:
        save_path {String} -- the path where CSV file is saved
        file_name {String} -- CSV file name
        query_result {List} -- query result

    Returns:
        Boolean -- return true if CSV file is saved successfully
    """

    try:
        # export query to csv file
        query_result.to_csv(file_path, index=False)
        # return true if CSV file is successfully saved
        return True
    except:
        # return false if fail to save the file
        return False


if __name__ == "__main__":
    connection = database.get_db_connection("root", "12345678", "world")
    # query.printDB(query.get_DBinfo())
    results = query.manual_sql_query(
        connection, "select Name, District from city")
    exportCSV("E:\project", "test.csv", results)
