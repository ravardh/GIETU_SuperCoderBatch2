class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
def traverse(root):
    if(root==None):
        return
    traverse(root.left)
    print(root.data,end="")
    traverse(root.right)
def preorder(root):
    if(root==None):
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if(root==None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end="")

def levelorder(root):
    Q=[]
    Q.push(root)
    Q.push(None)
    
    while Q:
        cur=Q.pop()
        if cur:
            print(cur.data)
        elif Q.empty():
            return
        else:
            Q.push(None)
        if Q.left:
            Q.append()
        if Q.right:
            Q.

root=node(1)
root.left=node(2)
root.right=node(4)
root.left.left=node(19)
root.left.right=node(14)
root.right.left=node(6)
root.right.right=node(12)
root.left.right.left=node(9)
root.left.right.right=node(5)
root.right.left.right=node(16)
root.right.right.left=node(8)
root.right.right.right=node(11)
root.left.right.left.right=node(10)
root.right.right.left.left=node(15)
root.right.right.right.left=node(17)
root.right.right.right.right=node(20)

print(root)
print(root.data)
traverse(root)
preorder(root)
postorder(root)