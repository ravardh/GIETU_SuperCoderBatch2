class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)
if __name__ == "__main__":
    root = None
    keys = [5, 3, 7, 2, 4, 6, 8]

    for key in keys:
        root = insert(root, key)

    print("Inorder traversal:")
    inorder_traversal(root)   
