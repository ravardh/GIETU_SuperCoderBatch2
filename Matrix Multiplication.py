def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Matrices are not compatible for multiplication.")
        return None

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = None
            while element is None:
                element_str = input(f"Enter element for row {i+1} column {j+1}: ")
                if element_str.isdigit():
                    element = int(element_str)
                else:
                    print("Invalid input. Please enter a valid integer.")
            row.append(element)
        matrix.append(row)
    return matrix

valid_input = False
while not valid_input:
    rows1_str = input("Enter the number of rows for matrix 1: ")
    cols1_str = input("Enter the number of columns for matrix 1: ")
    rows2_str = input("Enter the number of rows for matrix 2: ")
    cols2_str = input("Enter the number of columns for matrix 2: ")

    if rows1_str.isdigit() and cols1_str.isdigit() and rows2_str.isdigit() and cols2_str.isdigit():
        rows1, cols1, rows2, cols2 = map(int, (rows1_str, cols1_str, rows2_str, cols2_str))
        if cols1 == rows2:
            valid_input = True
        else:
            print("Error")
    else:
        print("Invalid")

print("Enter elements for matrix 1:")
matrix_a = input_matrix(rows1, cols1)

print("Enter elements for matrix 2:")
matrix_b = input_matrix(rows2, cols2)

result_matrix = matrix_multiply(matrix_a, matrix_b)

if result_matrix:
    print("Result: ")
    for row in result_matrix:
        print(row)
