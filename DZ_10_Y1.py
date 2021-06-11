class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_str = ''
        for item in self.matrix:
            for item_index in range(len(item)):
                matrix_str += f'{item[item_index]}'
            matrix_str += '\n'
        return matrix_str

    def __add__(self, other):
        new_matrix = []
        for first_matrix_item, second_matrix_item in zip(
                self.matrix, other.matrix

        ):
            new_row = []
            for index in range(len(first_matrix_item)):
                sum_of_elements = \
                    first_matrix_item[index] + second_matrix_item[index]
                new_row.append(sum_of_elements)
            new_matrix.append(new_row)
        return Matrix(new_matrix)


if __name__ == '__main__':
    mtx1 = Matrix([[1, 4, 3], [3, 4, 5], [6, 3, 8]])
    mtx2 = Matrix([[1, 4, 3], [3, 4, 5], [6, 3, 8]])
    print(mtx1)
    print(mtx2)
    mtx3 = mtx1 + mtx2
    print(mtx3)
