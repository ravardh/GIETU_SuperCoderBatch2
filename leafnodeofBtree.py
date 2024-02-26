class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def findLeafNodes(root, leaf_nodes):
    if root is None:
        return
    if root.left is None and root.right is None:
        leaf_nodes.append(root.val)
    findLeafNodes(root.left, leaf_nodes)
    findLeafNodes(root.right, leaf_nodes)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)

leaf_nodes = []
findLeafNodes(root, leaf_nodes)

print("Leaf nodes of the binary tree are:", leaf_nodes)
