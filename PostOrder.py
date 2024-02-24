class TreeNode:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
    
def PostOrder(root,list):
    if(root==None):
        return
       
    PostOrder(root.left,list)
    PostOrder(root.right,list)
    list.append(root.val)

list=[]
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

PostOrder(root,list)
print(list)
