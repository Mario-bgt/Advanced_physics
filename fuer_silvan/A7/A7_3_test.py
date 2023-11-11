#!/usr/bin/env python3
from unittest import TestCase
from A7_3 import move


# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class MoveTestSuite(TestCase):

    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        # uncomment the following line once you've implemented move
        self.assertEqual(expected, actual)

    def test_move_up(self):
        # NOTE: this test case is buggy and needs fixing!
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "up")
        expected = (
            (
                "#####   ",
                "### o  #",
                "#     ##",
                "   #####"
            ),
            ('down', 'left', 'right')
        )
        # uncomment the following line once you've implemented move
        self.assertEqual(expected, actual)

    def test_move_down(self):
        state = (
            "#####   ",
            "### o  #",
            "#     ##",
            "   #####"
        )
        actual = move(state, "down")
        expected = (
            (
                "#####   ",
                "###    #",
                "#   o ##",
                "   #####"
            ),
            ('left', 'right', 'up')
        )
        # uncomment the following line once you've implemented move
        self.assertEqual(expected, actual)

    def test_move_left(self):
        state = (
            "#####   ",
            "### o  #",
            "#     ##",
            "   #####"
        )
        actual = move(state, "left")
        expected = (
            (
                "#####   ",
                "###o   #",
                "#     ##",
                "   #####"
            ),
            ('down', 'right')
        )
        # uncomment the following line once you've implemented move
        self.assertEqual(expected, actual)

    def test_move_invalid_state(self):
        state = (
            "#####   ",
            "### o  #",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_wrong_character(self):
        state = (
            "###N#   ",
            "### o  #",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_not_same_length(self):
        state = (
            "######   ",
            "### o  #",
            "#     ##",
            "   ####"
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_too_many_players(self):
        state = (
            "#####   ",
            "### o  #",
            "# o   ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_no_possible_moves(self):
        state = (
            "#####   ",
            "###o#   #",
            "#  #  ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_invalid_dimension(self):
        state = (
            "",
            "",
            "",
            ""
        )
        with self.assertRaises(Warning):
            move(state, "left")

    def test_exceed_boundaries(self):
        state = (
                "###o  ",
                "###   ",
                "#    #",
                "    ##"
            )
        with self.assertRaises(Warning):
            move(state, "up")
