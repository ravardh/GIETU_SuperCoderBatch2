class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
L=[0]
def rightView(root,CL,L):
    if root is None:
        return
    if(L[0]<CL):
        print(root.data)
        L[0]=CL
    rightView(root.right,CL+1,L)
    rightView(root.left,CL+1,L)

root=node(1)
root.left=node(5)
root.right=node(7)
root.left.left=node(2)
root.left.right=node(4)
root.right.right=node(17)
root.left.left.left=node(20)
root.left.left.left.right=node(10)
root.left.left.left.right.left=node(21)
root.left.right.left=node(11)
root.left.right.right=node(3)
root.right.right.left=node(12)
root.right.right.right=node(16)
root.left.right.left.left=node(14)
root.left.right.left.right=node(19)
root.left.right.left.right.right=node(18)
root.left.right.left.right.right.right=node(15)

rightView(root,1,L)
