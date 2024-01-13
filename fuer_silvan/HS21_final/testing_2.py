import unittest


class MyTestSuite(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            l1, l2 = dict_to_lists("Ich bin ein string")

    def test_sorted(self):
        l1, l2 = dict_to_lists({"a": 20, "z": 1, "b": 8})
        res = sorted(["a", "z", "b"])
        self.assertTrue(res == l1)

    def test_simple_example(self):
        self.assertTrue(dict_to_lists({"b": 1, "a": 2}) == (["a", "b"], [2, 1]))

    def test_types(self):
        l1, l2 = dict_to_lists({"a": 20, "z": 1, "b": 8})
        self.assertTrue(type(l1) == list)
        self.assertTrue(type(l2) == list)


