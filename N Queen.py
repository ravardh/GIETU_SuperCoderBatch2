#N-Queen Problem

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    if col == len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1):
                return True

            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0):
        print("No solution exists.")
    else:
        print("Solution:")
        for row in board:
            print(" ".join(map(str, row)))

def get_board_size():
    while True:
        n = input("Enter the board size (n): ")
        if n.isdigit() and int(n) > 0:
            return int(n)
        else:
            print("Please enter a positive integer.")

n = get_board_size()
solve_n_queens(n)
