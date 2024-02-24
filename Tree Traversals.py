class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def printPreOrder(root):
    if (root == None):
        return
    print(root.data,end=" ")
    printPreOrder(root.left)
    printPreOrder(root.right)
    
def printPostOrder(node):
    if(node==None):
        return
    printPostOrder(node.left)
    printPostOrder(node.right)
    print(node.data,end=" ")

def printInOrder(node):
    if(node==None):
        return
    printInOrder(node.left)
    print(node.data,end=" ")
    printInOrder(node.right)

def levelorder(root):
    if root is None:
        return
    
    Q = [root]

    while Q:
        level_length = len(Q)
        for _ in range(level_length):
            cur = Q.pop(0)
            print(cur.data, end=" ")
            
            if cur.left:
                Q.append(cur.left)
            if cur.right:
                Q.append(cur.right)
        print()
        
root = Node(1)
root.left = Node(2)
root.right= Node(4)

root.left.left = Node(3)
root.left.right = Node(6)

root.right.right= Node(7)
root.right.left= Node(5)

#print(root.data)
print("Pre Order Traversal")
printPreOrder(root)
print()
print("Post Order Traversal")
printPostOrder(root)
print()
print("In Order Traversal")
printInOrder(root)
print()
print("Level Order Traversal")
levelorder(root)