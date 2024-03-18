direction = "DLRU"
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]
def is_valid(row, col, n, maze):
    return 0 <= row < n and 0 <= col < n and maze[row][col] == 1
def find_path(row,col,maze,n,ans,current_path):
    if row == n - 1 and col == n - 1:
        ans.append(current_path)
        return
    maze[row][col] = 0
    for i in range(4):
        next_row = row + dr[i]
        next_col = col + dc[i]
        if is_valid(next_row, next_col, n, maze):
            current_path += direction[i]
            find_path(next_row, next_col, maze, n, ans, current_path)
            current_path = current_path[:-1]
    maze[row][col] = 1
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
n = len(maze)
result = []
current_path = ""
if maze[0][0] != 0 and maze[n - 1][n - 1] != 0:
    find_path(0, 0, maze, n, result, current_path)
if not result:
    print(-1)
else:
    print(" ".join(result))