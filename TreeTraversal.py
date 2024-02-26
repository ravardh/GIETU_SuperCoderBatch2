class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None 
def preorder(root):
    if root == None:
        return -1
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root == None:
        return -1
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
def postorder(root):
    if root == None:

        
        return -1
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
root= Node(1)
root.left=Node(2)
root.right=Node(4)
root.left.left=Node(3)
root.left.right=Node(6)   
root.right.left=Node(5)
root.right.right=Node(7)
print(root.data)
print("Preorder Traversal")
print(preorder(root))
print("Inorder Traversal")
print(inorder(root))
print("Postorder Traversal")
print(postorder(root))
