import unittest
import os

from .exercise_2 import (
    current_program,
    find_program,
    load_csv,
    parse_timestamp,
)


class TestFindProgram(unittest.TestCase):

    def test_happy(self):
        """
        For example, given the inputs:

        tv_schedule_1.csv
        "2016-01-26 21:03:09"

        The output should be "Silent Witness" and 189.
        """
        result = find_program('tv_schedule_1.csv', '2016-01-26 21:03:09')

        expected_result = 'Silent Witness 189'

        self.assertEqual(result, expected_result)


class TestParseTimestamp(unittest.TestCase):

    def test_happy(self):
        """
        2016-01-26 21:03:09 should be 1453842189
        """
        self.assertEqual(parse_timestamp('2016-01-26 21:03:09'), 1453842189)


class TestCurrentProgram(unittest.TestCase):

    def test_no_data(self):
        """
        Latest program with no data will be None
        """
        result = current_program([], 1234)

        self.assertIsNone(result)

    def test_happy(self):
        """
        Latest programw when you get to the end is the last one
        """
        data = [
            (100, 'the dawn of time'),
            (200, 'middle'),
            (300, 'end of the world'),
        ]

        result = current_program(data, 101)

        self.assertEqual(result, ('the dawn of time 1'))

    def test_happy_too(self):
        """
        Latest program when you get to the end is the last one
        """
        data = [
            (100, 'the dawn of time'),
            (200, 'middle'),
            (300, 'end of the world'),
        ]

        result = current_program(data, 50)

        self.assertEqual(result, 'end of the world')


class LoadCSV(unittest.TestCase):

    def test_happy(self):
        """
        Given path return tuple of time and show name
        """
        file_name = os.path.join(os.path.dirname(__file__), 'test.csv')
        result = load_csv(file_name)

        expected_result = [
            (1453788000, 'Breakfast'),
            (1453799700, 'The Housing Enforcers'),
        ]

        self.assertEqual(result, expected_result)
