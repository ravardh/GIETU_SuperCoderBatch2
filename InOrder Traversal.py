class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def Inorder(root):
        if root:
            Inorder(root.left)
            print(root.data)
            Inorder(root.right)
if __name__=="__main__":
        root=Node(1)
        root.left=Node(2)
        root.right=Node(3)
        root.left.left=Node(4)
        root.left.right=Node(5)
        root.right.left=Node(6)
        root.right.right=Node(7)
print("Inorder Traversal")
Inorder(root)
        

        
