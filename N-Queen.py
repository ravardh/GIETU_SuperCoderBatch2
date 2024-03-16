def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, N):
                return True
            board[i][col] = 0
    return False

def print_solution(board,N):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()

def main():
    N = 8
    board = [[0] * N for _ in range(N)]
    if solve_n_queens(board, 0, N):
        print("Solution exists:")
        print_solution(board, N)
    else:
        print("Solution does not exist!")


main()