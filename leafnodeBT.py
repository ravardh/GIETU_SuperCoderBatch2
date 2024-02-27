class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def LeafNode(root):
    if root == None:
        return 0
    if(root.left == None and root.right == None):
        print(root.data)
    if root.left != None:
        LeafNode(root.left)
    if root.right != None:
        LeafNode(root.right)
root= Node(1)
root.left=Node(2)
root.right=Node(4)
root.left.left=Node(3)
root.left.right=Node(6)   
root.right.left=Node(5)
root.right.right=Node(7)
LeafNode(root)
        
        