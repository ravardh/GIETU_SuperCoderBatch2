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

    # Use a queue to perform level order traversal
    queue = deque()
    queue.append(root)
    hd_dict = {}  # Dictionary to store the horizontal distance of nodes

    # Set the horizontal distance of the root node to 0
    root.hd = 0

    while queue:
        node = queue.popleft()
        hd = node.hd  # Horizontal distance of the current node

        # If the horizontal distance is not in the dictionary, add it
        if hd not in hd_dict:
            hd_dict[hd] = node.key

        # Enqueue the left child with a horizontal distance one less than current
        if node.left:
            node.left.hd = hd - 1
            queue.append(node.left)

        # Enqueue the right child with a horizontal distance one more than current
        if node.right:
            node.right.hd = hd + 1
            queue.append(node.right)

    # Print the nodes in the top view
    for key in sorted(hd_dict.keys()):
        print(hd_dict[key], end=" ")

# Example usage:
# Constructing the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

print("Top view of the binary tree:")
top_view(root)
