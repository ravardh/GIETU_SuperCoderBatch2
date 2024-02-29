class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
def findHeight(root):
   if(root==None):
       return 0
   return max(findHeight(root.left),findHeight(root.right))+1


def levelorder(root):
    Q=[root]
    Q.append(None)
    while Q:
        cur = Q.pop(0)
        if cur:
            print(cur.data,end=" ")
            if cur.left:
                Q.append(cur.left)
            if cur.right:
                Q.append(cur.right)
        elif len(Q)==0:
            return
        else:
            Q.append(None)
            print()
root = node(20)
root.left = node(32)
root.right = node(10)
root.left.left = node(15)
root.left.right = node(12)
root.right.left = node(8)
root.right.right = node(24)
root.left.left.left = node(4)
root.left.right.left = node(50)
root.left.right.right= node(6)
root.left.right.left.left= node(40)
root.left.right.left.right = node(35)
root.right.right.left= node(16)
root.right.right.right = node(2)
print("the tree is:-")
levelorder(root)
print()
print("The height of the tree is:-",findHeight(root))