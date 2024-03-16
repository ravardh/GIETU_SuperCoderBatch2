# N-Queen Problem

def arrange_position(n: int, idx: int, board: list):
    if idx >= n:
        return True

    for i in range(n):
        if is_safe(idx, i, board):
            board[idx][i] = 1
            if arrange_position(n, idx + 1, board):
                return True
            board[idx][i] = 0

    return False


def is_safe(i: int, j: int, board: list) -> bool:
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 1:
                if x == i or y == j:
                    return False

                if x - i == y - j:
                    return False

                if i - x == y - j:
                    return False

    return True


if __name__ == '__main__':
    n: int = 5
    board: list = [[0 for j in range(n)] for i in range(n)]

    arrange_position(n, 0, board)
    for row in board:
        for element in row:
            print(element, end='\t')
        print()