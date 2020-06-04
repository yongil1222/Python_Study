def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x
                for x in [len(vector) for vector in vector_variables[1:]])


def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [sum(elements) for elements in zip(*vector_variables)]


def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    return [elements[0]*2-sum(elements)
            for elements in zip(*vector_variables)]


def scalar_vector_product(alpha, vector_variable):
    return [alpha * element for element in vector_variable]


def matrix_size_check(*matrix_variables):
    return all([len(set(len(matrix[0]) for matrix in matrix_variables)) == 1]) and all([len(matrix_variables[0]) == len(matrix) for matrix in matrix_variables])


def is_matrix_equal(*matrix_variables):
    return all([all([len(set(row)) == 1 for row in zip(*matrix)]) for matrix in zip(*matrix_variables)])


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [[sum(row) for row in zip(*matrix)] for matrix in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return [ [row[0]*2 - sum(row) for row in zip(*matrix)] for matrix in zip(*matrix_variables)]


def matrix_transpose(matrix_variable):
    return [ [ element for element in row] for row in zip(*matrix_variable)]


def scalar_matrix_product(alpha, matrix_variable):
    return [ scalar_vector_product(alpha, row) for row in matrix_variable ]


def is_product_availability_matrix(matrix_a, matrix_b):
    return len([column_vector for column_vector in zip(*matrix_a)]) == len(matrix_b)


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    return [[sum(a*b for a,b in zip(row_a, column_b)) 
            for column_b in zip(*matrix_b)] 
            for row_a in matrix_a]
