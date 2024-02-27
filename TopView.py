class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.key=None
def top_view(root):
    if(root==None):
        return
    Q=[root]
    key=0
    TV=dict()
    root.key=key
    while len(Q)!=0:
        curr=Q.pop(0)
        key=curr.key
        if key not in TV:
            TV[key]=curr.data
        if curr.left != None:
            Q.append(curr.left)
            curr.left.key=key-1
        if curr.right != None:
            Q.append(curr.right)
            curr.right.key=key+1
    for x in sorted(TV.keys()):
        print(TV[x],end="")

root=node(2)
root.left=node(6)
root.right=node(10)
root.left.left=node(15)
root.left.right=node(26)
root.right.left=node(21)
root.right.right=node(22)
