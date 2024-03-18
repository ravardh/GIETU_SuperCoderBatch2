global N
N=4
def solution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                print("1",end="")
            else:
                print("-1",end="")
        print()
def place(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
def solve(board,col):
    if col>=N:
        return True
    for i in range(N):
        if place(board,i,col):
            board[i][col]=1
            if solve(board,col+1)==True:
                return True
            board[i][col]=0
    return False
def main():
    board=[[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    if solve(board,0)==False:
        return False
    solution(board)
    return True
if __name__ == '_main_':
    main()