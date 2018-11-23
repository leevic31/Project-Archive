import unittest
import pyxl

class Testparse_xlsx(unittest.TestCase):

    def test_01_no_columns(self):
        file_name = ''
        column_names = []
        row_start = 1
        row_end = 3

        expected = []
        result = pyxl.parse_xlsx(file_name, column_names, row_start, row_end)
        self.assertEqual(expected, result, "empty column list fails")

    def test_02_single_row(self):
        file_name = 'pyxl_test_02.xlsx'
        column_names = ['A', 'B', 'C']
        row_start = 1
        row_end = 2
        expected = [['Bob', 'Joe', 'Alice']]
        result = pyxl.parse_xlsx(file_name, column_names, row_start, row_end)
        self.assertEqual(expected, result, "one row fails")

    def test_03_multiple_rows(self):
        file_name = 'pyxl_test_03.xlsx'
        column_names = ['A', 'B', 'C']
        row_start = 1
        row_end = 3
        expected = [['Bob', 'Joe', 'Alice'], ['Ada', 'Cobol', 'C']]
        result = pyxl.parse_xlsx(file_name, column_names, row_start, row_end)
        self.assertEqual(expected, result, "multiple rows fails")

    def test_04_negative_range(self):
        file_name = 'pyxl_test_03.xlsx'
        column_names = ['A', 'B', 'C']
        row_start = 10
        row_end = 4
        expected = []
        result = pyxl.parse_xlsx(file_name, column_names, row_start, row_end)
        self.assertEqual(expected, result, "negative range fails")

if (__name__ == '__main__'):
    unittest.main(exit=False)
