import csv
import database
import query
from os import path
import pandas as pd
import numpy as np


def exportCSV(save_path, file_name, query_result):
    """Export the query  result into CSV file

    Arguments:
        save_path {String} -- the path where CSV file is saved
        file_name {String} -- CSV file name
        query_result {List} -- query result

    Returns:
        Boolean -- return true if CSV file is saved successfully
    """

    # setup file location
    location = path.join(save_path, file_name)
    # to save the column name from query result
    column = list()
    data = list()
    first = False
    if query_result:
        for record in query_result:
            for key in record.keys():
                column.append(key)
            break
        df = pd.DataFrame(columns=column)
        for record in query_result:
            temp = pd.DataFrame([record], columns=record.keys())
            df = pd.concat([df, temp], axis=0, sort=True)
        df.to_csv(location, index=False)
        return True
    else:
        return False


if __name__ == "__main__":
    connection = database.get_db_connection("root", "12345678", "world")
    # query.printDB(query.get_DBinfo())
    results = query.manual_sql_query(
        connection, "select * from country where continent ='Asia'")
    exportCSV("E:\project", "test.csv", results)
