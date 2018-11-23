import database
import query
from os import path
import pandas as pd

class ExportCSV:
    def export(self, file_path, query_text):
        '''(ExportCSV, str, str) -> None
        Given a file path and sql query, export the data from that sql query
        into a csv format.

        Arguments:
            file_path {str}  -- CSV file name
            query_text {str} -- query string

        Returns:
            None
        '''
        conn = database.get_db_connection()
        # export query to csv file
        dataframe = query.manual_sql_query(conn, query_text)
        if (not file_path.endswith(".csv")):
            file_path += ".csv"
        dataframe.to_csv(file_path, index=False)

if __name__ == "__main__":
    connection = database.get_db_connection("root", "12345678", "world")
    # query.printDB(query.get_DBinfo())
    results = query.manual_sql_query(
        connection, "select Name, District from city")
    exportCSV("E:\project", "test.csv", results)
