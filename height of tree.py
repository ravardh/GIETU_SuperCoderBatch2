class tree:
    def __init__(self,key):
        self.right=None
        self.left=None
        self.val=key
        
def height(root):
    if not root:
        return 0
    left_height=height(root.left)
    right_height=height(root.right)
    
    return max(left_height,right_height)+1

def leaf(root):
    if root==None:
        return
    elif root.left==None and root.right==None:
        print(root.val, end=" ")
    else:
        leaf(root.left)
        leaf(root.right)

root=tree(1)
root.left=tree(2)
root.right=tree(3)
root.left.left=tree(4)
root.left.right=tree(5)
root.right.left=tree(6)
root.right.right=tree(7)

tree_height=height(root)
print(tree_height)

no_of_leaf=leaf(root)
