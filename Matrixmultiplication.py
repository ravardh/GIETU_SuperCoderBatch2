def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrices cannot be multiplied. Inner dimensions must match.")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j]+=A[i][k]*B[k][j]
    return result

def input_matrix(rows, cols):
    matrix = []
    print("Enter matrix elements:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element for row {i+1}, column {j+1}: "))
            row.append(element)
        matrix.append(row)
    return matrix

rows_A = int(input("Enter number of rows for matrix A: "))
cols_A = int(input("Enter number of columns for matrix A: "))

rows_B = int(input("Enter number of rows for matrix B: "))
cols_B = int(input("Enter number of columns for matrix B: "))

print("For matrix A:")
A = input_matrix(rows_A, cols_A)

print("For matrix B:")
B = input_matrix(rows_B, cols_B)

try:
    result = matrix_multiply(A, B)
    print("Result of matrix multiplication:")

    for row in result:
        print(row)
except ValueError as e:
    print(e)
