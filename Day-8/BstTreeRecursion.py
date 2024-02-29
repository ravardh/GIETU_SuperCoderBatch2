class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if data<root.data:
        if root.left == None:
            root.left=Node(data)
            return
        else:
            insert(root.left,data)

    if data > root.data:
        if root.right == None:
            root.right = Node(data)
            return
        else:
            insert(root.right, data)
def preOrder_traversal(root):
    if root:
        preOrder_traversal(root.left)
        print(root.data,end=' ')
        preOrder_traversal(root.right)

array = [50,36,39,66,75,19,98,76,105,22,42,21]
root = Node(array[0])
for data in range (1,len(array)):
    insert(root,array[data])
print("prerder Traversal:")
preOrder_traversal(root)
