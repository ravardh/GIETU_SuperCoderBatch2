def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, 4)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    if row == 4:
        return True

    for col in range(4):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

chessboard = [[0] * 4 for _ in range(4)]

if solve_n_queens(chessboard, 0):
    for i in range(4):
        for j in range(4):
            if chessboard[i][j] == 0:
                chessboard[i][j] = -1
else:
    print("No solution exists for 4x4 N-Queens problem.")

print_board(chessboard)
