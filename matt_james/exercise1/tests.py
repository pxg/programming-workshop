import unittest
import os

from .exercise_1 import (
    current_program,
    find_program,
    load_csv,
)


class TestFindProgram(unittest.TestCase):

    def test_happy(self):
        """
        For example, given the inputs:

        tv_schedule_1.csv 1453805100 The output should be "Homes Under the
        Hammer" which started at 1453802400, or 26th January 2016 at 10:00. The
        input timestamp 1453805100 converts to 10:45 on 26th January 2016. The
        next show, "Wanted Down Under", starts at 1453806000, or 26th January
        2016 at 11:00
        """
        result = find_program('tv_schedule_1.csv', 1453805100)

        expected_result = "Homes Under the Hammer"

        self.assertEqual(result, expected_result)


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

        self.assertEqual(result, 'the dawn of time')

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

        self.assertIsNone(result)


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
