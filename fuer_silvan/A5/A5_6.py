#!/usr/bin/env python3
from unittest import TestCase
from task.script import median


# Extend the test suite with regression tests that cover the
# meaningful bug reports. Make sure that you define test methods
# and that each method _directly_ includes an assertion in the
# body, or -otherwise- the grading will mark the test suite as
# invalid.
class MedianTests(TestCase):
    def test_1(self):
        """User 1: Super annoying! I collect all my bills in a list, only yesterday,
        I paid 5.90 for my Latte Macchiato. When I use your function to calculate
        the median, it simply does not work!? It returns numbers that are not even
        in the list... I don't understand what I am doing wrong."""
        testlist = [1, 2, 5.90, 7]
        actual = median(testlist)
        expected = 3.95
        self.assertEqual(actual, expected)

    def test_2(self):
        """User 2: The median is defined for two cases. If "the middle" points to an
        actual index, it should be used, but when it falls "between" two values,
        the average should be used."""
        testlist = [1, 2, 3, 4]
        actual = median(testlist)
        expected = 2.5
        self.assertEqual(actual, expected)

    def test_3(self):
        """User 2: The median is defined for two cases. If "the middle" points to an
        actual index, it should be used, but when it falls "between" two values,
        the average should be used."""
        testlist = [1, 2, 3, 4, 5]
        actual = median(testlist)
        expected = 3
        self.assertEqual(actual, expected)

    def test_4(self):
        """User 4: Just because I don't have enough values in my list does not mean
        that your function can crash. It happens. Every. Time. I am furious! Wouldn't
        'None' be a good default?"""
        testlist = []
        actual = median(testlist)
        expected = None
        self.assertEqual(actual, expected)
