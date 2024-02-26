class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def findDepth(root):
    if root is None:
        return 0
    return max(findDepth(root.left), findDepth(root.right)) + 1

def findLeafNodes(root):
    leaf_nodes = []

    def dfs(node):
        if node is not None:
            if node.left is None and node.right is None:
                leaf_nodes.append(node.data)
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return leaf_nodes

root = Node(20)
root.left = Node(30)
root.right = Node(40)
root.left.left = Node(50)
root.left.right = Node(60)
root.right.left = Node(70)
root.right.right = Node(80)
root.left.left.left = Node(90)
root.left.left.right = Node(100)

print("Depth of the Binary tree is:", findDepth(root))
print("Leaf nodes of the Binary tree are:", findLeafNodes(root))
