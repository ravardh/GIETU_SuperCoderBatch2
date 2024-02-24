class TreeNode:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
    
def InOrder(root,list):
    if(root==None):
        return
    
    InOrder(root.left,list)
    list.append(root.val)
    InOrder(root.right,list)

list=[]
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

InOrder(root,list)
print(list)
