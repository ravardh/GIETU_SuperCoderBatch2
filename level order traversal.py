
class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Creating a sample binary tree
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)

# Performing level-order traversal without using def keyword
queue = [root]  # Using a list as a queue
while queue:
    current_node = queue.pop(0)
    print(current_node.val, end=" ")

    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)
