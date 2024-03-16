# Example matrices
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Check if number of columns in the first matrix equals number of rows in the second matrix
if len(matrix_A[0]) != len(matrix_B):
    raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

# Initialize the result matrix with appropriate dimensions
result = [[0] * len(matrix_B[0]) for _ in range(len(matrix_A))]

# Perform matrix multiplication
for i in range(len(matrix_A)):
    for j in range(len(matrix_B[0])):
        for k in range(len(matrix_B)):
            result[i][j] += matrix_A[i][k] * matrix_B[k][j]

# Print the input matrices and the result of their multiplication
print("Matrix A:")
for row in matrix_A:
    print(row)

print("\nMatrix B:")
for row in matrix_B:
    print(row)

print("\nResult of matrix multiplication:")
for row in result:
    print(row)
