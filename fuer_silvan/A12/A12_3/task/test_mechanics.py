#!/usr/bin/env python3

from unittest import TestCase
from knight import Knight
from rogue import Rogue

class TestBattle(TestCase):

    def test_basic_attack(self):
        sut = Knight("Arthur", 3)
        actual = sut.get_health()
        expected = (150, 150)
        self.assertEqual(expected, actual)

    def test_knight_attack(self):
        k = Knight("Arthur", 3)
        r = Rogue("Shades", 3)
        k.attack(r)
        actual = r.get_health()[0]
        expected = 150 - round(0.8*(3*10+0))
        self.assertEqual(expected, actual)

