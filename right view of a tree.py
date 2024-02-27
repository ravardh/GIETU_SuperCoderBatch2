L=[0]
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def rightView(root,value,L):
    CL=value
    if root is None:
        return
    if(L[0]<CL):
        print(root.data,end=" ")
        L[0]=CL
    rightView(root.right,CL+1,L)
    rightView(root.left,CL+1,L)
         

root = Node(1)

root.left = Node(5)
root.right=Node(7)

root.left.left=Node(2)
root.left.right=Node(4)

root.left.left.left=Node(20)
root.left.right.left=Node(11)

root.left.right.right=Node(3)

root.left.left.left.right=Node(10)
root.left.left.left.right.left=Node(21)

root.right.right=Node(17)
root.right.right.left=Node(12)
root.right.right.right=Node(16)

root.right.right.left.left=Node(14)
root.right.right.left.right=Node(19)

root.right.right.left.right.right=Node(18)
root.right.right.left.right.right.right=Node(15)

print("Right View of Binary Tree")
rightView(root,1,L)
