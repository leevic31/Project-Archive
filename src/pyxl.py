import sys

import openpyxl
import openpyxl.utils

def iCare_parse_columns(file_name):
    book = openpyxl.load_workbook(filename = file_name, read_only = True)

    sheet = book.active

    columns = []
    row = 3

    for i in range(1, sheet.max_column + 1):
        cell = "{}{}".format(openpyxl.utils.get_column_letter(i), row)
        columns.append(sheet[cell].value)

    return columns

def parse_xlsx(file_name, column_names, row_start, row_end):
    '''(str, list of str, int, int) -> list of list of str
    
    '''
    column_len = len(column_names)
    if (column_len <= 0):
        return []

    book = openpyxl.load_workbook(filename = file_name, read_only = True)
    sheet = book.active

    values = []
    for row in range(row_start, row_end):
        values.append([cell.value for cell in sheet[row]])

    return values
