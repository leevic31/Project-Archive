import database
import query
from os import path
import pandas as pd


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
