from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.hd = 0  

def topView(root):
    if root is None:
        return

    top_view_map = {}

    queue = deque()
    queue.append(root)

    while queue:
        current_node = queue.popleft()
        hd = current_node.hd
        
        if hd not in top_view_map:
            top_view_map[hd] = current_node.key

        if current_node.left:
            current_node.left.hd = hd - 1
            queue.append(current_node.left)

        if current_node.right:
            current_node.right.hd = hd + 1
            queue.append(current_node.right)

    for key in sorted(top_view_map):
        print(top_view_map[key], end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)


print("Top view of the binary tree:")
topView(root)
