class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
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
root = node(1)
root.left = node(2)
root.right = node(4)
root.left.left = node(19)
root.left.right = node(14)
root.right.left = node(6)
root.right.right = node(12)
root.left.right.left = node(9)
root.left.right.right = node(5)
root.left.right.left.right = node(10)
root.right.left.right = node(16)
root.right.right.left = node(8)
root.right.right.right = node(11)
root.right.right.left.left = node(15)
root.right.right.right.left = node(17)
root.right.right.right.right = node(20)

print(root)
print(root.data)


print("Level order Traversal")
levelorder(root)