#depth of binary tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0
    else:
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)
        return max(left_depth, right_depth) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Depth of the binary tree is:", max_depth(root))
