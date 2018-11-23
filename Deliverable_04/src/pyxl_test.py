import unittest
from pyxl import *

class Testpyxl(unittest.TestCase):

    def test_01_blank_tables(self):
        # start with two tables that will be empty
        t1 = Table()
        t2 = Table()
        # the result of the cartesian product of two empty tables
        # should iteslf be an empty table
        result = squeal.cartesian_product(t1, t2)
        # we'll know it's an empty table if its dictionary is empty
        result_dict = result.get_dict()
        expected = {}
        self.assertEqual(result_dict, expected,
                         "product of two empty tables should be empty")

    def test_02_first_table_blank(self):
        books = {'book.author': ['Douglas Hofstadter', 'Randall Munroe',
                                 'Randall Munroe', 'Andrew Hodges'],
                 'book.year': ['1979', '2014', '2015', '2014'],
                 'book.title': ['Godel Escher Bach',
                                'What if?',
                                'Thing Explainer',
                                'Alan Turing: The Enigma']}

        # Start with two empty tables
        t1 = Table()
        t2 = Table()

        # Fill the second table with content
        t2.set_dict(books)

        result = squeal.cartesian_product(t1, t2)
        result_dict = result.get_dict()
        expected = {'book.author': [], 'book.year': [], 'book.title': []}
        self.assertEqual(result_dict, expected,
                         "product of one empty table and one " +
                         "non-empty table should be table with all " +
                         "the table columns but empty column values")

    def test_03_second_table_blank(self):
        books = {'book.author': ['Douglas Hofstadter', 'Randall Munroe',
                                 'Randall Munroe', 'Andrew Hodges'],
                 'book.year': ['1979', '2014', '2015', '2014'],
                 'book.title': ['Godel Escher Bach',
                                'What if?',
                                'Thing Explainer',
                                'Alan Turing: The Enigma']}

        # Start with two empty tables
        t1 = Table()
        t2 = Table()

        # Fill the second table with content
        t1.set_dict(books)

        result = squeal.cartesian_product(t1, t2)
        result_dict = result.get_dict()
        expected = {'book.author': [], 'book.year': [], 'book.title': []}
        self.assertEqual(result_dict, expected,
                         "product of one empty table and one " +
                         "non-empty table should be table with all " +
                         "the table columns but empty column values")

    def test_04_each_table_one_row(self):
        books = {'book.author': ['Douglas Hofstadter'],
                 'book.year': ['1979'],
                 'book.title': ['Godel Escher Bach']}

        movies = {'m.year': ['1997'],
                  'm.title': ['Titanic'],
                  'm.studio': ['Par.'],
                  'm.gross': ['2186.8']}

        # Start with two empty tables
        t1 = Table()
        t2 = Table()

        # Fill the Tables with content
        t1.set_dict(books)
        t2.set_dict(movies)

        result = squeal.cartesian_product(t1, t2)
        result_dict = result.get_dict()
        expected = {'book.author': ['Douglas Hofstadter'],
                    'book.year': ['1979'],
                    'book.title': ['Godel Escher Bach'],
                    'm.year': ['1997'],
                    'm.title': ['Titanic'],
                    'm.studio': ['Par.'],
                    'm.gross': ['2186.8']}

        self.assertEqual(result_dict, expected,
                         "product of one empty table and one " +
                         "non-empty table should be table with all " +
                         "the table columns but empty column values")

        movies = {'m.year': ['1997', '2003', '2010'],
                  'm.title': ['Titanic', \
                  'The Lord of the Rings: The Return of the King', \
                  'Toy Story 3'],
                  'm.studio': ['Par.', 'NL', 'BV'], \
                  'm.gross': ['2186.8', '1119.9', '1063.2']}

    def test_05(self):
        self.assertEqual(0, 0.0, "WRONG")


if (__name__ == '__main__'):
    unittest.main(exit=False)
