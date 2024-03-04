from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.hd = None  # Horizontal distance from the root

def top_view(root):
    if not root:
        return

    queue = deque()
    queue.append(root)
    hd_dict = {}  # Dictionary to store the horizontal distance of nodes

    root.hd = 0

    while queue:
        node = queue.popleft()
        hd = node.hd  # Horizontal distance of the current node

        if hd not in hd_dict:
            hd_dict[hd] = node.key

        if node.left:
            node.left.hd = hd - 1
            queue.append(node.left)

        if node.right:
            node.right.hd = hd + 1
            queue.append(node.right)
    for key in sorted(hd_dict.keys()):
        print(hd_dict[key], end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

print("Top view of the binary tree:")
top_view(root)
