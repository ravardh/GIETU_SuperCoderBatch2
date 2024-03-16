def matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        print("Error: Number of columns in matrix A must be equal to number of rows in matrix B")
        return None

    result = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result_matrix = matrix_multiplication(matrix1, matrix2)
if result_matrix:
    print("Result of matrix multiplication:")
    for row in result_matrix:
        print(row)
