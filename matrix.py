def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    if cols1 != rows2:
        raise ValueError("Invalid number of elements")
    
    result = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3]
]

result_matrix = matrix_multiplication(matrix1, matrix2)

print("Resultant Matrix:")
for row in result_matrix:
    print(row)
