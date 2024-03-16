# def chess(p):
#     for i in p:
#         for j in i:
#             print(j,end=' ')
#         print()
# p=list([[0]*4 for _ in range(4)])
# # print(type(p))
# def change(p):
#     for i in range(len(p)):
#         for j in range(len(p[i])):
#             if (i+1)!=1 and (i+2)!=1 and (i+3)!=1 and (j+1)!=1 and (j+2)!=1 and (j+3)!=1:
#                 p[i][j]=1
#     # for i in range(len(p)):
#     #     for j in range(len(p[i])):
#     #         if p[i][j]==0:
#     #             p[i][j]=1
#     #             for x in range(max(0,i-1),min(len(p),i+2)):
#     #                 for y in range(max(0,j-1),min(len(p[i]),j+2)):
#     #                     p[x][y]=1
# change(p)
# chess(p)
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