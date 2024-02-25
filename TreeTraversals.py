class node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key


def Inorder(root):
    if root == None:
        return
    Inorder(root.left)
    print(root.val)
    Inorder(root.right)

def Preorder(root):
    if root == None:
        return
    print(root.val)
    Preorder(root.left)
    Preorder(root.right)

def Postorder(root):
    if root == None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.val)


if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(4)
    root.left.left = node(19)
    root.left.right = node(14)
    root.right.left = node(6)
    root.right.right = node(12)
    root.left.right.left = node(9)
    root.left.right.right = node(5)
    root.left.right.left.right = node(10)
    root.right.left.right = node(16)
    root.right.right.left = node(8)
    root.right.right.right = node(11)
    root.right.right.left.left = node(15)
    root.right.right.right.left = node(17)
    root.right.right.right.right = node(20)
    print("inorder traversal of tree is: ")
    print(Inorder(root))
    print("preorder traversal of tree is: ")
    print(Preorder(root))
    print("postorder traversal of tree is: ")
    print(Postorder(root))
