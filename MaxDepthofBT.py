class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def Finddepth(root):
    if root == None:
        return 0
    return max(Finddepth(root.left),Finddepth(root.right))+1
root= Node(1)
root.left=Node(2)
root.right=Node(4)
root.left.left=Node(3)
root.left.right=Node(6)   
root.right.left=Node(5)
root.right.right=Node(7)
print("Maximum Depth of the Binary Tree ",Finddepth(root))
