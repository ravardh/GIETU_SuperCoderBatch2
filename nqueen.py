def is_safe(board,row,col,M):
    for i in range(row):
        if board[i][col]==1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,-1-1)):
        if board[i][j]==1:
            return False
        
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
        
    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, N):
                return True
            board[row][col] = 0

    return False

def solve_n_queen(N):
    board = [[0] * N for _ in range(N)]

    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))

n = 4  
solve_n_queen(n)