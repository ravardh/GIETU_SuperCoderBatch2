class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.key = None

def TopView(root):
    if(root == None):
        return
    Q=[root]
    key=0
    Top=dict()
    root.key=key
    while Q:
        cur = Q.pop(0)
        key=cur.key
        if key not in Top:
            Top[key]=cur.data
        if cur.left !=None:
            Q.append(cur.left)
            cur.left.key=key-1
        if cur.right !=None:
            Q.append(cur.right)
            cur.right.key = key +1
    for i in sorted(Top.keys()):
        print(Top[i],end=" ")
        
def BottomView(root):
    if(root == None):
        return
    Q=[root]
    key=0
    Top=dict()
    root.key=key
    dict2={}
    while Q:
        cur = Q.pop(0)
        key=cur.key
        dict2[key]=cur.data
        if cur.left !=None:
            Q.append(cur.left)
            cur.left.key=key-1
        if cur.right !=None:
            Q.append(cur.right)
            cur.right.key = key +1
    for i in sorted(dict2.keys()):
        print(dict2[i],end=" ")
L=[0]
def leftView(root,CL,L):
    if root is None:
        return
    if(L[0]<CL):
        print(root.data)
        L[0]=CL
    leftView(root.left,CL+1,L)
    leftView(root.right,CL+1,L)

def rightView(root,CL,L):
    if root is None:
        return
    if(L[0]<CL):
        print(root.data)
        L[0]=CL
    rightView(root.right,CL+1,L)
    rightView(root.left,CL+1,L)


root = node(20)
root.left = node(32)
root.right = node(10)
root.left.left = node(15)
root.left.right = node(12)
root.right.left = node(8)
root.right.right = node(24)
root.left.left.left = node(4)
root.left.right.left = node(50)
root.left.right.right = node(6)
root.left.right.left.left = node(40)
root.left.right.left.right = node(35)
root.right.right.left = node(16)
root.right.right.right = node(2)

print("The Top view of the tree is: ",end="")
TopView(root)
print()
print("The Bottom view of the tree is: ",end="")
BottomView(root)
print()
print("The Left view of the tree is: ",end="")
leftView(root,1,L)
print()
print("The Right view of the tree is: ",end="")
rightView(root,1,L)
