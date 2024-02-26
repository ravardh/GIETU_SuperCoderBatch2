class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def findHeight(node):
    if node == None:
        return 0
    height = max(findHeight(node.left),findHeight(node.right))+1
    return height
    
root = Node(1)
root.left = Node(2)
root.right= Node(4)

root.left.left = Node(3)
root.left.right = Node(6)

root.right.right= Node(7)
root.right.left= Node(5)


print("Hegiht of the given tree is",findHeight(root))
