class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.hd = 0

def top_view(root):
    if root is None:
        return

    top_view_map = {}
    queue = []
    queue.append(root)

    while queue:
        temp = queue.pop(0)
        hd = temp.hd

        if hd not in top_view_map:
            top_view_map[hd] = temp.data

        if temp.left:
            temp.left.hd = hd - 1
            queue.append(temp.left)

        if temp.right:
            temp.right.hd = hd + 1
            queue.append(temp.right)

    for key in sorted(top_view_map):
        print(top_view_map[key], end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

print("Top view of the binary tree:")
top_view(root)
