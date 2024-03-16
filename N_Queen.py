def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col + row:
            return False
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append(list(board))
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)

def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

n = int(input("Enter the value of n: "))
solutions = solve_n_queens(n)
print("Total solutions:", len(solutions))
