class Matrix:
    def __init__(self, matrix):
        if not isinstance(matrix, list):
            raise AssertionError("Matrix must be a list")
        if not isinstance(matrix[0], list):
            raise AssertionError("Matrix must be a list of lists")
        for row in matrix:
            for element in row:
                if not isinstance(element, int) and not isinstance(element, float):
                    raise AssertionError("Matrix must only contain numbers")
        if len(matrix) < 1:
            raise AssertionError("Matrix must not be empty")
        if matrix == [[]]:
            raise AssertionError("Matrix must not be empty")
        self.__matrix = matrix

    # Remember that instanes variables should be private (i.e., prepended with two underscores: __)

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise AssertionError("Can only add matrices to matrices")
        if len(self.__matrix) != len(other.__matrix) or len(self.__matrix[0]) != len(other.__matrix[0]):
            raise AssertionError("Matrices must have compatible dimensions")
        new_matrix = []
        for i in range(len(self.__matrix)):
            new_row = []
            for j in range(len(self.__matrix[0])):
                new_row.append(self.__matrix[i][j] + other.__matrix[i][j])
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise AssertionError("Can only multiply matrices to matrices")
        if len(self.__matrix[0]) != len(other.__matrix):
            raise AssertionError("Matrices must have compatible dimensions")
        new_matrix = []
        for i in range(len(self.__matrix)):
            new_row = []
            for j in range(len(other.__matrix[0])):
                new_element = 0
                for k in range(len(self.__matrix[0])):
                    new_element += self.__matrix[i][k] * other.__matrix[k][j]
                new_row.append(new_element)
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if self.__matrix == other.__matrix:
            return True
        else:
            return False

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.__matrix))

    def get_matrix(self):
        return self.__matrix


matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6, 7], [8, 9, 10], [11, 12, 13]])
result_matrix = matrix1 * matrix2
print(result_matrix.get_matrix())
