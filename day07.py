class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Depth of a Binary Tree
def maxDepth(root):
    if not root:
        return 0

    lh = maxDepth(root.left)
    rh = maxDepth(root.right)

    return 1 + max(lh, rh)

# Print the leaf nodes
def printLeaves(root):
    if not root:
        return
    elif not root.left and not root.right:
        print(root.val, end = ' ')
    
    if root.left: printLeaves(root.left)
    if root.right: printLeaves(root.right)

# Top View
def topView(root):
    if not root:
        return
    
    hash_map = {}
    queue = [(root, 0)]

    while queue:
        node, line = queue.pop(0)

        if line not in hash_map:
            hash_map[line] = node.val
        if node.left:
            queue.append((node.left, line - 1))
        if node.right:
            queue.append((node.right, line + 1))

    for value in sorted(hash_map.keys()):
        print(hash_map[value], end = ' ')

# Bottom View
def bottomView(root):
  if not root:
    return
  hash_map = {}
  queue_of_nodes = [(root, 0)]

  while queue_of_nodes:
    node, line = queue_of_nodes.pop(0)
    hash_map[line] = node.data

    if node.left:
      queue_of_nodes.append((node.left, line - 1))
    if node.right:
      queue_of_nodes.append((node.right, line + 1))
    
  for value in sorted(hash_map.keys()):
    print(hash_map[value], end=" ")


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

print("Leaf nodes in the binary tree:")
printLeaves(root)
print('\nThe top view is: ')
topView(root)
print('\nThe bottom view is: ')
topView(root)