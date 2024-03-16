def is_safe(board,row,col,n):
    for i in range(row):
        if board[i]==col or abs(board[i]-col)==row-i:
            return False
    return True

def solve_util(board, row, n, sol):
    if row == n:
        sol.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_util(board, row + 1, n, sol)

def solve_n_queens(n):
    board =[-1]*n
    sol=[]
    solve_util(board, 0, n, sol)
    if not sol:
        print("Solution does not exist")
        return False
    print("Number of solutions:", len(sol))
    for i in sol:
        print(i)

n =int(input("Enter the number: ")) 
solve_n_queens(n)
