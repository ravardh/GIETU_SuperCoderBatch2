class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue[0]
        print(node.data)
        queue = queue[1:]

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(22)
    root.right = Node(53)
    root.left.left = Node(84)
    root.left.right = Node(88)
    root.right.left = Node(63)
    root.right.right = Node(97)

    print("Level Order Traversal: ", end="")
    printLevelOrder(root)
