import unittest
from A9_3 import Matrix


class TestMatrixClass(unittest.TestCase):

    def test_matrix_creation(self):
        matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix = Matrix(matrix_data)
        self.assertEqual(matrix.get_matrix(), matrix_data)

    def test_add_matrices(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result_matrix = matrix1 + matrix2
        expected_matrix = Matrix([[6, 8], [10, 12]])
        self.assertEqual(result_matrix, expected_matrix)

    def test_add_incompatible_matrices(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6, 7], [8, 9, 10]])
        with self.assertRaises(AssertionError):
            result_matrix = matrix1 + matrix2

    def test_multiply_matrices(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        result_matrix = matrix1 * matrix2
        expected_matrix = Matrix([[19, 22], [43, 50]])
        self.assertEqual(result_matrix, expected_matrix)

    def test_multiply_incompatible_matrices(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6, 7], [8, 9, 10], [11, 12, 13]])
        with self.assertRaises(AssertionError):
            result_matrix = matrix1 * matrix2


    def test_matrix_equality(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[1, 2], [3, 4]])
        self.assertEqual(matrix1, matrix2)

    def test_matrix_inequality(self):
        matrix1 = Matrix([[1, 2], [3, 4]])
        matrix2 = Matrix([[5, 6], [7, 8]])
        self.assertNotEqual(matrix1, matrix2)

    def test_invalid_matrix_creation(self):
        with self.assertRaises(AssertionError):
            invalid_matrix = Matrix("invalid")

    def test_empty_matrix_creation(self):
        with self.assertRaises(AssertionError):
            empty_matrix = Matrix([])


if __name__ == '__main__':
    unittest.main()