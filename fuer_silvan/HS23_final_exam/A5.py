def process(string, needle, mode="remove", character=None):
    if len(needle) < 1:
        raise ValueError
    if mode not in ["remove", "replace"]:
        raise NameError
    if mode == "replace" and character is None:
        raise TypeError
    if mode == "replace":
        return string.replace(needle, character)
    if mode == "remove":
        return string.replace(needle, "")

# examples of how process can be used:
print( process("abcd_abcd", "b", "remove") )       # acd_acd
print( process("abcd_abcd", "b", "replace", "*") ) # a*cd_a*cd
from unittest import TestCase
class Tests(TestCase):

    def test_needle_to_short(self):
        with self.assertRaises(ValueError):
            process("abcd", [])

    def test_wrong_mode(self):
        with self.assertRaises(NameError):
            process("abcd", "b", "adjust")

    def test_type_error(self):
        with self.assertRaises(TypeError):
            process("abcd", "b", "replace")

    def test_replace(self):
        actual = process("abcd", "b", "replace", "*")
        expected = "abcd".replace("b", "*")
        self.assertEqual(actual, expected)

    def test_remove(self):
        actual = process("abcd_abcd", "b", "remove")
        expected = "abcd_abcd".replace("b", "")
        self.assertEqual(actual, expected)




