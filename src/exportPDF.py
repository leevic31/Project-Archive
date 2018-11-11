import exportFile
import database
import query
from os import path
import pandas as pd
import pdfkit
import os
import query

def exportToPDF(file_name, query_result):
    """Export the query result into PDF file
    
    Arguments:
        file_name {String} -- PDF file name
        query_result {List} -- query result

    Returns:
        Boolean -- return true if PDF file is saved successfully
        
    """
    try:
        # export query result to html
        query_result.to_html('result.html')
        # convert query result from html to pdf
        pdfkit.from_file('result.html', file_name)
        # delete the saved html
        os.remove('result.html')
        # return true if PDF file is successfully saved
        return True
    except:
        # return false if fail to save the file
        return False
