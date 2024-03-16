def main():

    n = 4
    board = []
    for j in range(n):
        row = []
        for i in range(n):
            row.append('X')
        board.append(row)

        nqueen(board, 0)


def nqueen(board, row):
    n = len(board)
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
        print()
        return

    for j in range(n):
        if is_safe(board, row, j):
            board[row][j] = 'Q'
            nqueen(board, row + 1)
            board[row][j] = 'X'


def is_safe(board, row, col):
    n = len(board)
    for j in range(n):
        if board[row][j] == 'Q':
            return False

    for i in range(n):
        if board[i][col] == 'Q':
            return False

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    i, j = row, col
    while i < n and j < n:
        if board[i][j] == 'Q':
            return False
        i += 1
        j += 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    return True


main()