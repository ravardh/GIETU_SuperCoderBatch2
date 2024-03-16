class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.key = None

def rightView(root,value,l):
    if(root==None):
        return
    cl=value
    if(l[0]<cl):
        print(root.data,end=" ")
        l[0]=cl

    rightView(root.right, cl + 1, l)
    rightView(root.left, cl + 1, l)
def levelorder(root):
    Q = [root]
    Q.append(None)
    while Q:
        cur = Q.pop(0)
        if cur:
            print(cur.data, end=" ")
            if cur.left:
                Q.append(cur.left)
            if cur.right:
                Q.append(cur.right)
        elif len(Q) == 0:
            return
        else:
            Q.append(None)
            print()


root = node(1)
root.left = node(5)
root.right = node(7)
root.left.left = node(2)
root.left.right = node(4)
root.left.left.left = node(20)
root.left.left.left.right = node(10)
root.left.left.left.right.left = node(21)
root.left.right.left = node(11)
root.left.right.right = node(3)
root.right.right= node(17)
root.right.right.left = node(12)
root.right.right.right = node(16)
root.right.right.left.left = node(14)
root.right.right.left.right = node(19)
root.right.right.left.right.right = node(18)
root.right.right.left.right.right.right = node(15)
l=[0]
print("the tree is:-")
levelorder(root)
print()
print("The right view of the tree is:-")
rightView(root,1,l)