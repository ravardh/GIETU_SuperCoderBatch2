L=[0]
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def leftView(root,value,L):
    CL=value
    if root is None:
        return
    if(L[0]<CL):
        print(root.data,end=" ")
        L[0]=CL
    leftView(root.left,CL+1,L)
    leftView(root.right,CL+1,L)
    
root = Node(1)
root.left = Node(2)
root.right= Node(4)

root.left.left = Node(3)
root.left.right = Node(6)

root.right.right= Node(7)
root.right.left= Node(5)

print("Left View of Binary Tree")
leftView(root,1,L)
