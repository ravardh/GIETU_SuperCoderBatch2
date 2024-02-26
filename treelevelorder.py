class node:
    def _init_(self,data=None):
        self.data=data
        self.left=None
        self.right=None

def top(root):
    if (root==None):
        return 0
    Q=[root]
    key=0
    tv=dict()
    root.key=key
    while len(Q)!=0:
        curr=Q.pop(0)
        key=curr.key
        if key not in tv:
            tv[key]=curr.data
        if curr.left!=None:
            Q.append(curr.left)
            curr.left.key=key-1
        if curr.right!=None:
            Q.append(curr.right)
            curr.right.key=key+1
            
    for x in sorted(tv.keys()):
            print(tv[x])
            
root=node(20)
root.left=node(32)
root.right=node(10)
root.left.left=node(15)
root.left.right=node(12)
root.right.left=node(8)
root.right.right=node(24)
root.right.right.left=node(16)
root.right.right.right=node(2)
root.left.left.left=node(4)
root.left.right.left=node(50)
root.left.right.left.left=node(40)
root.left.right.left.right=node(35)
root.left.right.left=node(6)

print(top(root))