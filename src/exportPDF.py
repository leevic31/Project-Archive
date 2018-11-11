import exportFile
import database
import query
from os import path
import pandas as pd
import pdfkit
import os

def exportToPDF(file_name, query_result):
    try:
        query_result.to_html('result.html')
        pdfkit.from_file('result.html', file_name)
        os.remove('result.html')
        return True
    except:
        return False
    
if __name__ == "__main__":
    connection = database.get_db_connection_with("world", "root", "")
    results = query.manual_sql_query(
        connection, "select Name, District from city")
    exportToPDF("result.pdf", results)

