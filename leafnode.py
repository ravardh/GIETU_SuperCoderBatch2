class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def print_leaf_nodes(root):
    if root:
        # If the node is a leaf, print its value
        if root.left is None and root.right is None:
            print(root.val)
        # Traverse left and right subtrees
        print_leaf_nodes(root.left)
        print_leaf_nodes(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Leaf nodes:")
print_leaf_nodes(root)