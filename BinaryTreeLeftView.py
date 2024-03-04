class node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

root=node(1)
root.left=node(5)
root.right=node(7)
root.left.left=node(2)
root.left.right=node(4)
root.right.right=node(17)
root.left.left.left=node(20)
root.left.right.left=node(11)
root.left.right.right=node(3)
root.right.right.left=node(12)
root.right.right.right=node(16)
root.left.left.left.right=node(10)
root.right.right.left.left=node(14)
root.right.right.left.right=node(19)
root.left.left.left.right.left=node(21)
root.right.right.left.right.right=node(18)
root.right.right.left.right.right.right=node(15)



L =[0]
def leftView(root,value,L):
    if root == None:
        return 
    cl = value
    if(L[0]<cl):
        print(root.data)
        L[0] = cl
        leftView(root.left,cl+1,L)
    leftView(root.right,cl+1,L)
    
leftView(root,1,L)