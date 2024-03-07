#Depth of a binary tree.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def maxDepth(root):
    if root is None:
        return 0
    else:
        # Compute the depth of each subtree
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)

        # Use the larger depth and add 1 for the current node
        return max(left_depth, right_depth) + 1


# Example usage:
# Constructing a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Calculate and print the depth of the binary tree
depth = maxDepth(root)
print("Depth of the binary tree is:", depth)
