class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

def LeftView(root,value,L):
    if(root==None):
        return
    cl=value
    if(L[0]<cl):
        print(root.data)
        L[0]=cl
    LeftView(root.left,cl+1,L)
    LeftView(root.right,cl+1,L)

root=node(1)
root.left=node(5)
root.left.left=node(2)
root.left.left.left=node(20)
root.left.left.left.right=node(10)
root.left.left.left.right.left=node(21)
root.left.right=node(4)
root.left.right.left=node(11)
root.left.right.right=node(3)
root.right=node(7)
root.right.right=node(17)
root.right.right.left=node(12)
root.right.right.left.left=node(14)
root.right.right.right=node(16)
root.right.right.left.right=node(19)
root.right.right.left.right.right=node(18)
root.right.right.left.right.right.right=node(15)
L=[0]
a=LeftView(root,1,L)
print(a)