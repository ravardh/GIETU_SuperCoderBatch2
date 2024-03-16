class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
def findheight(root):
    if root==None:
        return 0
    return max(findheight(root.left),findheight(root.right))+1
def leafnode(root):
    if root==None:
        return
    if(root.left is None and root.right is None):
        print(root.data,end=" ")
    if root.left is not None:
        leafnode(root.left)
    if root.right is not None:
        leafnode(root.right)
def topview(root):
    if(root==None):
        return
    Q=[root]
    key=0
    view=dict()
    root.key=key
    while len(Q)!=0:
        curr=Q.pop(0)
        key=curr.key
        if key not in view:
            view[key]=curr.data
        if curr.left !=None:
            Q.append(curr.left)
            curr.left.key=key-1
        if curr.right!=None:
            Q.append(curr.right)
            curr.right.key=key+1
    for x in sorted(view.keys()):
         print(view[x],end=" ")
    print()
root=node(1)
root.left=node(2)
root.right=node(4)
root.left.left=node(19)
root.left.right=node(14)
root.right.left=node(6)
root.right.right=node(12)
root.left.right.left=node(9)
root.left.right.right=node(5)
root.left.right.left.right=node(10)
root.right.left.right=node(16)
root.right.right.left=node(8)
root.right.right.right=node(11)
root.right.right.left.left=node(15)
root.right.right.right.left=node(17)
root.right.right.right.right=node(20)
print(findheight(root))
leafnode(root)
topview(root)