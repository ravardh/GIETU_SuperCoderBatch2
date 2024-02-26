# Tree traversal in Python


class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):

    if root:
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)

def postorder(root):

    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end='')

def preorder(root):

    if root:
        print(str(root.val) + "->", end='')
        preorder(root.left)
        preorder(root.right)

def LevelOrder(root):
 
    if root is None:
        return
    queue = []
    queue.append(root)
 
    while(len(queue) > 0):
 
        print(queue[0].val, end=" ")
        node = queue.pop(0)
 
        if node.left is not None:
            queue.append(node.left)
 
        if node.right is not None:
            queue.append(node.right)
 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)

print("\nLevel order traversal")
LevelOrder(root)
