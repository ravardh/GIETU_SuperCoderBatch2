class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        # Traverse left
        inorder_traversal(root.left)
        # Visit the root
        print(root.val)
        # Traverse right
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        # Visit the root
        print(root.val)
        # Traverse left
        preorder_traversal(root.left)
        # Traverse right
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        # Traverse left
        postorder_traversal(root.left)
        # Traverse right
        postorder_traversal(root.right)
        # Visit the root
        print(root.val)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal:")
inorder_traversal(root)

print("\nPreorder traversal:")
preorder_traversal(root)

print("\nPostorder traversal:")
postorder_traversal(root)
