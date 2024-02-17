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
        