"""You are given a correct implementation of a function upper_lower_capitalize, which takes a string as a
parameter string and returns a tuple with 3 values: string in upper case, string in lower case, and string with
only the first letter in upper case.
Write a test suite that can identify faulty implementations exhibiting the following problems:
The upper case string is wrong
The lower case string is wrong
The capitalized string is wrong
Implement exactly 3 tests. For an implementation exhibiting exactly one of the isolated faults listed above, exactly
 one test must fail while the other two must pass.
You may want to introduce bugs into upper_lower_capitalize to check whether your test suite works correctly.
Submit your entire Test class as given in the template and do not change its name. Do not submit the
 upper_lower_capitalize function.
Use the following template:"""


def upper_lower_capitalize(string):
    return string.upper(), string.lower(), string.capitalize()


from unittest import TestCase


class TestSuite(TestCase):
    def test_upper_case(self):
        expected = "ELEFANT"
        actual = upper_lower_capitalize("Elefant")[0]
        self.assertEqual(expected, actual)

    def test_lower_case(self):
        expected = "elefant"
        actual = upper_lower_capitalize("Elefant")[1]
        self.assertEqual(expected, actual)

    def test_captialize_case(self):
        expected = "Elefant"
        actual = upper_lower_capitalize("elefant")[2]
        self.assertEqual(expected, actual)
