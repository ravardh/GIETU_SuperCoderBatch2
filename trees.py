class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

def levelorder(root):
    if root is None:
        return
    
    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Inorder Traversal:")
inorder(root)
print("\n")

print("Preorder Traversal:")
preorder(root)
print("\n")

print("Postorder Traversal:")
postorder(root)
print("\n")

print("Level Order Traversal:")
levelorder(root)
