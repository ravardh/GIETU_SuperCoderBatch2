class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None


def findheight(root):

    if root==None:
        return 0
    height=max(findheight(root.left),findheight(root.right))+1
    return height


L=[0]
def leftViewUse(root, cl, L):
    if root is None:
        return
 
    if (L[0] < cl):
        print (root.data, end = " ")
        L[0] = cl
 
    leftViewUse(root.left, cl + 1, L)
    leftViewUse(root.right, cl + 1, L)
 

def rightViewUse(root, cl, L):
    if root is None:
        return
 
    if (L[0] < cl):
        print (root.data, end = " ")
        L[0] = cl
 
    rightViewUse(root.left, cl + 1, L)
    rightViewUse(root.right, cl + 1, L)



 
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

print(findheight(root))

leftViewUse(root,1,L)

rightViewUse(root,1,L)

#print(findNodes(root))

