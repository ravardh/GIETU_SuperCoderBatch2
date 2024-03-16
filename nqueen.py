def isSafe(board,row,col):
      # print("inside check")
  # col
  for i in range(len(board)):
    if(board[row][i]==1):
      return False
  # row
  for i in range(len(board)):
    if(board[i][col]==1):
      return False
  
  # lower left
  j = col
  for i in range(row, len(board)):
    if j >= 0:
      if board[i][j] == 1:
          return False
    j=j-1
  
  #uper left
  j = col
  for i in range(row, -1, -1):
    if j >= 0:
      if board[i][j] == 1:
          return False
    j=j-1

  #uper right
  j = col
  for i in range(row, -1, -1):
    if j <len(board):
      if board[i][j] == 1:
          return False
    j=j+1
  #lower right
  j = col
  for i in range(row,len(board)):
    if j <len(board):
      if board[i][j] == 1:
          return False
    j=j+1
  return True
def addsol(AnsBoard,board):
    newBoard = []
    for i in range(len(board)):
        row = ""
        for j in range(len(board[i])):
            if board[i][j] == 1:
                row = row + '1'
            else:
                row = row + '0'
        newBoard.append(row)
    AnsBoard.append(newBoard)
def createBoard(AnsBoard,board,n,row):
  if(row==n):
    # for i in range(n):
    #   print(board[i])
    addsol(AnsBoard,board)
    return 
  for i in range(n):
    # print(isSafe(board,row,i))
    if(isSafe(board,row,i)):
      board[row][i]=1
      # print("queen added")
      # print(board)
      createBoard(AnsBoard,board,n,row+1)
      board[row][i]=0


def NQueen(n):
    AnsBoard=[]
    board = [[0 for _ in range(n)] for _ in range(n)] 
    # print(board)
    createBoard(AnsBoard,board, n, 0)
    return AnsBoard

n=int(input("Enter No of Queens"))
print(NQueen(n))
# NQueen(n)