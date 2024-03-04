class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.hd = None

def topView(root):
    if root is None:
        return
    q = [root]
    hd = 0
    top_view = {}
    root.hd = hd
    while len(q) != 0:
        curr = q.pop(0)
        hd = curr.hd
        if hd not in top_view:
            top_view[hd] = curr.data
        if curr.left is not None:
            q.append(curr.left)
            curr.left.hd = hd - 1
        if curr.right is not None:
            q.append(curr.right)
            curr.right.hd = hd + 1
    for key in sorted(top_view.keys()):
        print(top_view[key], end=" ")

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
print("Top view of the tree:")
topView(root)