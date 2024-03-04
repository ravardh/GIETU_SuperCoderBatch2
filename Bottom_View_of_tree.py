class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.key = None

def bottomView(root):
    if root is None:
        return
    q = [root]
    key = 0
    bView = dict()
    root.key = key
    while len(q) != 0:
        curr = q.pop(0)
        key = curr.key
        bView[key] = curr.data
        if curr.left is not None:
            q.append(curr.left)
            curr.left.key = key - 1
        if curr.right is not None:
            q.append(curr.right)
            curr.right.key = key + 1
    for x in sorted(bView.keys()):
        print(bView[x], end=" ")

root = Node(20)
root.left = Node(32)
root.right = Node(10)
root.left.left = Node(15)
root.left.right = Node(12)
root.right.left = Node(8)
root.right.right = Node(24)
root.left.left.left = Node(4)
root.left.right.left = Node(50)
root.left.right.right = Node(6)
root.right.right.left = Node(16)
root.right.right.right = Node(2)
root.left.right.left.left = Node(40)
root.left.right.left.right = Node(35)

print("Bottom view of the tree:")
bottomView(root)