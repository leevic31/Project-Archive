import exportFile
import database
import query
from os import path
import pandas as pd
import pdfkit
import os
import query

query_result = query.manual_sql_query(connection, command)

def exportToPDF(file_name, query_result):
    try:
        query_result.to_html('result.html')
        pdfkit.from_file('result.html', file_name)
        os.remove('result.html')
        return True
    except:
        return False
