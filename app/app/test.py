# python manage.py test is the command used for testing our code
# this command automaticallly checks for the file named test.py in our directory for unit test

from django.test import TestCase

from .calc import add, sub


class CalcTests(TestCase):
    # function name must start with test_ followed by any name
    # so that django will understand this is the code for unit test
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_sub_numbers(self):
        """Test that two numbers are subtracted together"""
        self.assertEqual(sub(8, 3), 5)
