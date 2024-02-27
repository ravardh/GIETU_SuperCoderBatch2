class node:
    def __init__(self,info=None):
        self.left=None
        self.data=info
        self.right=None
        self.key=None

def bottomView(root):
    if root is None:
        return
    Q = [root]
    key=0
    BView=dict()
    root.key=key
    while len(Q)!=0:
        curr=Q.pop(0)
        key=curr.key
        BView[key]=curr.data
        if curr.left!=None:
            Q.append(curr.left)
            curr.left.key=key-1
        if curr.right!=None:
            Q.append(curr.right)
            curr.right.key=key+1
    for x in sorted(BView.keys()):
        print(BView[x],end=" ")
root=node(20)
root.left=node(32)
root.right=node(10)
root.left.left=node(15)
root.left.right=node(12)
root.right.left=node(8)
root.right.right=node(24)
root.left.left.left=node(4)
root.left.right.left=node(50)
root.left.right.right=node(6)
root.right.right.left=node(16)
root.right.right.right=node(2)
root.left.right.left.left=node(40)
root.left.right.left.right=node(35)
bottomView(root)