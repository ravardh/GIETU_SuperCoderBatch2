def isSafe(board, r, c, n):
    # for same col
    for i in range(r):
        if board[i][c] == 1:
            return False
    # for upper left diag
    i, j = r, c
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # for upper right diag
    i, j = r, c
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def helper(board, r, n):
    if r == n:
        return True
    for c in range(n):
        if isSafe(board, r, c, n):
            board[r][c] = 1
            if helper(board, r + 1, n):
                return True
            board[r][c] = 0
    return False

def n_queen(n):
    board = [[0] * n for _ in range(n)]
    if not helper(board, 0, n):
        print("Solution does not exist")
        return

    for row in board:
        print(" ".join(map(str, row)))

n = int(input())
n_queen(n)
