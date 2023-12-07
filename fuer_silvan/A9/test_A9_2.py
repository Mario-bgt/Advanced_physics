import unittest
from A9_2 import Publication  # Import Publication class from your module

class TestPublication(unittest.TestCase):

    def test_initialization(self):
        authors = ["Gamma", "Helm", "Johnson", "Vlissides"]
        title = "Design Patterns"
        year = 1994
        pub = Publication(authors, title, year)
        self.assertEqual(pub.get_authors(), authors)
        self.assertEqual(pub.get_title(), title)
        self.assertEqual(pub.get_year(), year)

    def test_string_representation(self):
        authors = ["Duvall", "Matyas", "Glover"]
        title = "Continuous Integration"
        year = 2007
        pub = Publication(authors, title, year)
        expected_str = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
        self.assertEqual(str(pub), expected_str)

    def test_equality(self):
        p1 = Publication(["A"], "B", 1234)
        p2 = Publication(["A"], "B", 1234)
        p3 = Publication(["B"], "C", 2345)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p2, p3)

    def test_hashability(self):
        p1 = Publication(["A"], "B", 1234)
        p2 = Publication(["A"], "B", 1234)
        sales = {p1: 273}
        self.assertEqual(sales[p1], 273)
        self.assertEqual(sales[p2], 273)  # p2 should hash to the same value as p1

    def test_comparison_operators(self):
        p1 = Publication(["A"], "B", 1234)
        p2 = Publication(["B"], "C", 2345)
        self.assertTrue(p1 < p2)
        self.assertTrue(p1 <= p2)
        self.assertTrue(p2 > p1)
        self.assertTrue(p2 >= p1)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Publication("Incorrect", "Title", 1994)  # authors should be a list
        with self.assertRaises(TypeError):
            Publication(["Gamma", "Helm"], "Design Patterns", "1994")  # year should be an int


if __name__ == '__main__':
    unittest.main()
