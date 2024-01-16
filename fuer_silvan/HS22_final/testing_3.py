"""You are given a correct implementation of a function unique_sorted, which takes a list as a
 parameter values and returns a list containing all unique elements from values in descending order.
Write a test suite that can identify faulty implementations exhibiting the following problems:
An implementation that doesn't work correctly when given an empty list, but works correctly otherwise
An implementation that sorts the result, but does not remove duplicate values
An implementation that does remove duplicates, but does not sort the result
Implement exactly 3 tests. For an implementation exhibiting exactly one of the isolated faults listed above, exactly
one test must fail while the other two must pass.
You may want to introduce bugs into unique_sorted to check whether your test suite works correctly.
Submit your entire Test class as given in the template and do not change its name. Do not submit the unique_sorted
function.
Use the following template:
"""


def unique_sorted(values):
    return list(sorted(set(values), reverse=True))


from unittest import TestCase


class TestSuite(TestCase):
    def test_sorted_no_dublicates(self):
        lyst = [1, 4, 7, 2, 4, 1]
        lyst = sorted(lyst)
        res = unique_sorted(lyst)
        self.assertTrue(res == [1, 2, 4, 7])

    def test_try_empty(self):
        with self.assertRaises():
            unique_sorted([])

    def test_no_sorted_dublicates(self):
        lyst = [1, 4, 7, 2, 4, 1]
        lyst = [1, 4, 7, 2]
        res = unique_sorted(lyst)
        self.assertTrue(res == [1, 2, 4, 7])

