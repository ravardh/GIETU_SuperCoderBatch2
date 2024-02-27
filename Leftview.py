class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def Left_view(root, value, level):
    current_level = value
    if root is None:
        return
    if level[0] < current_level:
        print(root.data)
        level[0] = current_level
    Left_view(root.left, current_level + 1, level)
    Left_view(root.right, current_level + 1, level)

def left(root):
    level = [0]
    Left_view(root, 1, level)

root = node(1)
root.left = node(32)
root.right = node(10)
root.left.left = node(15)
root.left.right = node(12)
root.right.left = node(8)
root.right.right = node(24)

print(left(root))
