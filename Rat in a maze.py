def Valid_move(maze, row, col):
    rows = len(maze)
    cols = len(maze[0])
    return row >= 0 and col >= 0 and row < rows and col < cols and maze[row][col] == 1
def Solve_maze_util(maze,row,col,solution):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        solution[row][col] = 1
        return True
    if Valid_move(maze,row,col):
        solution[row][col] = 1
        if Solve_maze_util(maze,row + 1,col,solution):
           return True
        if Solve_maze_util(maze, row, col + 1, solution):
           return True
        solution[row][col]=0
        return False
def Solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])
    solution = [[0]*cols for _ in range(rows)]
    if not Solve_maze_util(maze,0,0,solution):
        print("No solution exists")
        return
    print("solution")
    for row in solution:
        print(row)
maze = [
    [1,0,0,1,0,0],
    [1,1,1,1,0,0],
    [0,1,0,1,0,1],
    [0,1,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,0,1]
]
Solve_maze(maze)

