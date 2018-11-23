from os import path

import pandas as pd
import pdfkit
import os

import exportCSV
import database
import query

class ExportPDF:
    def export(self, file_path, query_text):
        '''(ExportPDF, str, str) -> None
        Given a file path and sql query, export the data from that sql query
        into a pdf format.

        Arguments:
            file_path {str} -- PDF file name
            query_text {str} -- query string

        Returns:
            None
        '''

        conn = database.get_db_connection()
        dataframe = query.manual_sql_query(conn, query_text)
        # export query result to html
        dataframe.to_html('tmp.html')
        # convert query result from html to pdf
        if (not file_path.endswith(".pdf")):
            file_path += ".pdf"
        pdfkit.from_file('tmp.html', file_path)
        # delete the saved html
        os.remove('tmp.html')
