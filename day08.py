class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Left View
def leftView(root):
    if not root: return
    queue_of_nodes = [root]
    isPrinted = False

    while queue_of_nodes:
        for _ in range(len(queue_of_nodes)):
            node = queue_of_nodes.pop(0)
            if not isPrinted:
                print(node.val, end = ' ')
                isPrinted = True
            if node.left:
                queue_of_nodes.append(node.left)
            if node.right:
                queue_of_nodes.append(node.right)
        isPrinted = False

# Total nodes
def totalNodes(root):
    if not root:
        return 0
    return 1 + totalNodes(root.left) + totalNodes(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(8)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)
root.right.right.left = TreeNode(9)
root.right.right.right = TreeNode(10)

print('The left view: ')
leftView(root)
print('\nTotal nodes: ', totalNodes(root))
