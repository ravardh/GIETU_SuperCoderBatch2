class Node:
    def __init__(self,data):
        self.left=None
        self.right = None
        self.data = data
def RView(root):
    if root is None:
        return
    Q=[root]
    while Q:
        n = len(Q)
        for i in range(1,n+1):
            curr=Q.pop(0)
            if i ==n:
                print(curr.data, end=" ")
            if curr.left:
                Q.append(curr.left) 
            if curr.right:
                Q.append(curr.right)        

root = Node(1)
root.left = Node(5)
root.right = Node(7)

root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(17)

root.left.left.left = Node(20)
root.left.right.left = Node(11)
root.left.right.right = Node(3)
root.right.right.left = Node(12)
root.right.right.right = Node(16)

root.left.left.left.right = Node(10)
root.right.right.left.left = Node(14)
root.right.right.left.right = Node(19)
root.left.left.left.right.left = Node(21)
root.right.right.left.right.right = Node(18)

root.right.right.left.right.right.right = Node(15)
print("Right View Traversal:")
RView(root)

