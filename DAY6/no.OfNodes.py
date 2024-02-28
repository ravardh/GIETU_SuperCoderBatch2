# class node:
#     def __init__(self,data):
#         self.left=None
#         self.data=data
#         self.right=None
# def findnode(root):
#     if root==None:
#         return 
#     elif(root.left==None and root.right==None):
#         return
#     else:
#         print(root.data)
#     findnode(root.left)
#     findnode(root.right)
    
# root=node(1)
# root.left=node(5)
# root.right=node(7)
# root.left.left=node(2)
# root.left.right=node(4)
# root.right.right=node(17)
# root.left.left.left=node(20)
# root.left.left.left.right=node(10)
# root.left.left.left.right.left=node(21)
# root.left.right.left=node(11)
# root.left.right.right=node(3)
# root.right.right.left=node(12)
# root.right.right.right=node(16)
# root.right.right.left.left=node(14)
# root.right.right.left.right=node(19)
# root.right.right.left.right.right=node(18)
# root.right.right.left.right.right.right=node(15)

# findnode(root.left)
class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def countnode(root):
    if root==None:
        return 0 
    l=countnode(root.left)
    r=countnode(root.right)
    return 1+l+r
    
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
root.right.right.left.left=node(14)
root.right.right.left.right=node(19)
root.right.right.left.right.right=node(18)
root.right.right.left.right.right.right=node(15)

print(countnode(root))