def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True
def solve_n_queens(n):
    board = [[' '] * n for _ in range(n)]  # Initialize empty board
    def solve_util(board, row):
        if row == n:
            return True 
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q' 
                if solve_util(board, row + 1):  
                    return True
                board[row][col] = ' '  
        return False  
    if solve_util(board, 0):
        return board
    else:
        return None
def print_board(board):
    for row in board:
        print(' '.join(row))
while True:
    try:
        n = int(input("Enter board size (positive integer): "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
solution = solve_n_queens(n)
if solution:
    print("\nSolution Exists:")
    print_board(solution)
else:
    print("\nSolution does not exist for this configuration.")