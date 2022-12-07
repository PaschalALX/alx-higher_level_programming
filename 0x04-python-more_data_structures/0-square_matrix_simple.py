def square_matrix_simple(matrix):
    new_matrix = []

    for x in matrix:
        new_matrix.append(list(map(lambda x: x**2, x)))

    return new_matrix
