#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from character import Character


class Knight(Character):

    def __init__(self, name, lvl):
        super().__init__(name, lvl)


    def attack(self, other):
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_physical_damage(self._get_caused_dmg(other)*0.8)

    def _get_caused_dmg(self, other):
        # 10 * self._lvl + (self._lvl-other._lvl) = 11 * self._lvl - other._lvl
        return max(1, self._lvl * 11 - other._lvl)

    def _take_physical_damage(self, amount):
        assert isinstance(amount, int)
        assert amount >= 0
        self._health_cur = max(0, self._health_cur - amount*0.75)

