class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def left_view(root):
    left = []
    def inorder_traversal(node, level):
        nonlocal left
        if node is None:
            return
        if level == len(left):
            left.append(node.val)
        inorder_traversal(node.left, level + 1)
        inorder_traversal(node.right, level + 1)  
    inorder_traversal(root, 0)  
    return left

root = Node(30)
root.left = Node(17)
root.right = Node(12)
root.left.left = Node(13)
root.left.right = Node(19)
root.right.left = Node(7)
root.right.right = Node(28)
root.left.left.left = Node(3)
root.left.right.left = Node(35)
root.left.right.right = Node(4)
root.left.right.left.left = Node(40)
root.left.right.left.right =Node(40)
root.right.right.left = Node(22)
root.right.right.right = Node(2)

left_view_result = left_view(root)
print("Left view of the binary tree:", left_view_result)