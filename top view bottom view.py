class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        

def top_view(root):
    if root is None:
        return
    
    queue = []
    hd_node = {}
    queue.append((root, 0))

    while queue:
        node, hd = queue.pop(0)
        if hd not in hd_node:
            hd_node[hd] = node.key
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    for key in sorted(hd_node.keys()):
        print(hd_node[key], end=' ')


def bottom_view(root):
    if root is None:
        return
    
    queue = []
    hd_node = {}
    queue.append((root, 0))

    while queue:
        node, hd = queue.pop(0)
        hd_node[hd] = node.key
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    for key in sorted(hd_node.keys()):
        print(hd_node[key], end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

print("Top View:")
top_view(root)
print("\nBottom View:")
bottom_view(root)
