def sort(iterable):
    pass


from unittest import TestCase


"""
== Specification of `sort` ==
- takes an `Iterable` as a parameter that contains comparable elements
- sorts all contained elements without changing the original `Iterable`
- elements should be sorted in ascending order (i.e., smallest first)
- always returns a new `List` that contains the sorted elements
- If parameter is `None` or non-iterable, return  `None`.

The implementaion can assume that all elements of a provided iterable
are comparable data types (e.g., int, float, string). This means that
relational operations like '<', '>', etc. are defined. The behavior
for data types that are not comparable is not defined and they do not
need to be handled.
"""


class TestSortFunction(TestCase):

    def test_with_list_of_integers(self):
        self.assertEqual(sort([3, 1, 4, 1, 5, 9, 2]), [1, 1, 2, 3, 4, 5, 9])

    def test_with_list_of_floats(self):
        self.assertEqual(sort([3.1, 2.2, 1.3]), [1.3, 2.2, 3.1])

    def test_with_list_of_strings(self):
        self.assertEqual(sort(["banana", "apple", "cherry"]), ["apple", "banana", "cherry"])

    def test_with_tuple(self):
        self.assertEqual(sort((2.2, 1, 3.5)), [1, 2.2, 3.5])

    def test_with_empty_iterable(self):
        self.assertEqual(sort([]), [])

    def test_with_single_element(self):
        self.assertEqual(sort([42]), [42])

    def test_original_iterable_unchanged(self):
        original = [3, 1, 2]
        _ = sort(original)
        self.assertEqual(original, [3, 1, 2])

    def test_with_none(self):
        self.assertIsNone(sort(None))

    def test_with_non_iterable(self):
        self.assertIsNone(sort(123))


