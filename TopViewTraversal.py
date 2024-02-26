class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def TopView(root):
    if root is None:
        return

    Q = [root]
    key = 0
    TView = dict()
    root.key = key

    while len(Q) != 0:
        curr = Q.pop(0)
        key = curr.key

        if key not in TView:
            TView[key] = curr.data

        if curr.left is not None:
            Q.append(curr.left)
            curr.left.key = key - 1

        if curr.right is not None:
            Q.append(curr.right)
            curr.right.key = key + 1

    for x in sorted(TView.keys()):
        print(TView[x], end=" ")

root = Node(20)
root.left = Node(30)
root.right = Node(40)
root.left.left = Node(50)
root.left.right = Node(60)
root.right.left = Node(70)
root.right.right = Node(80)
root.left.left.left = Node(90)
root.left.right.left = Node(110)
root.right.right.left = Node(150)
root.right.right.right = Node(160)
root.left.right.left.left = Node(170)
root.left.right.left.right = Node(180)

TopView(root)
