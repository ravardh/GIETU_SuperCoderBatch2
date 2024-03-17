def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Matrix multiplication not possible. Number of columns in the first matrix must be equal to the number of rows in the second matrix."
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    return result
def input_matrix(prompt):
    matrix = []
    rows = int(input(prompt + " Enter the number of rows: "))
    columns = int(input(prompt + " Enter the number of columns: "))
    print("Enter the elements row-wise:")
    for i in range(rows):
        row = list(map(float, input().split()))
        if len(row) != columns:
            print("Invalid input! Please enter exactly", columns, "elements for each row.")
            return input_matrix(prompt)
        matrix.append(row)
    return matrix
if __name__ == "__main__":
    print("Matrix Multiplication")
    print("Enter the first matrix:")
    matrix1 = input_matrix("Matrix 1:")
    print("\nEnter the second matrix:")
    matrix2 = input_matrix("Matrix 2:")
    result = matrix_multiplication(matrix1, matrix2)
    if isinstance(result, str):
        print(result)
    else:
        print("\nResult of matrix multiplication:")
        for row in result:
            print(row)