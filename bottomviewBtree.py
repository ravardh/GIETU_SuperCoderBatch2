from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.hd = 0  

def bottomView(root):
    if root is None:
        return

    bottom_view_map = {}

    queue = deque()
    queue.append(root)

    while queue:
        current_node = queue.popleft()
        hd = current_node.hd

        bottom_view_map[hd] = current_node.key

        if current_node.left:
            current_node.left.hd = hd - 1
            queue.append(current_node.left)

        if current_node.right:
            current_node.right.hd = hd + 1
            queue.append(current_node.right)

    for key in sorted(bottom_view_map):
        print(bottom_view_map[key], end=" ")

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print("Bottom view of the binary tree:")
bottomView(root)
