
   # TOP VIEW OF A TREE
class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.key = None


def topView(root):
    q = [root]
    key = 0
    tView = dict()
    root.key = key
    while (len(q) != 0):
        curr = q.pop(0)
        key = curr.key
        if key not in tView:
            tView[key] = curr.data
        if curr.left != None:
            q.append(curr.left)
            curr.left.key = key - 1
        if curr.right != None:
            q.append(curr.right)
            curr.right.key = key + 1
    for x in sorted(tView.keys()):
        print(tView[x], end=" ")


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
root.right.right.left = node(16)
root.right.right.right = node(2)
root.left.right.left.left = node(40)
root.left.right.left.right = node(35)

topView(root)


