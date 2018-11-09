import database
import query
from os import path
import pandas as pd


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
    # save query result into dataframe
    df = pd.DataFrame(query_result)
    try:
        # export query to csv file
        df.to_csv(location, index=False)
        # return true if CSV file is successfully saved
        return True
    except:
        # return false if fail to save the file
        return False


if __name__ == "__main__":
    connection = database.get_db_connection("root", "12345678", "world")
    # query.printDB(query.get_DBinfo())
    results = query.manual_sql_query(
        connection, "select * from city")
    exportCSV("E:\project", "test.csv", results)
