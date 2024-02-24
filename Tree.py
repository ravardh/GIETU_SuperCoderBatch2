class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(3)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

def postorder(root):

    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)


def preorder(root):

    if root is None:
        return

    print(root.data)
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)
print("postorder traversal")
postorder(root)
print("preorder traversal")
preorder(root)
print("inorder traversal")
inorder(root)
