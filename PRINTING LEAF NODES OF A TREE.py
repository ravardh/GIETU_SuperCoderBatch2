class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def findHeight(node):
    if node == None:
        return 
    elif(not(node.left and node.right)):
        print(node.data,end=" ")
        return
    findHeight(node.left)
    findHeight(node.right)

    
root = Node(1)
root.left = Node(2)
root.right= Node(4)

root.left.left = Node(3)
root.left.right = Node(6)

root.right.right= Node(7)
root.right.left= Node(5)

print("Leaf nodes are :",end=" ")
findHeight(root)
