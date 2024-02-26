class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None
def levelordertraversal(root):
    if root == None:
        return 
    q=[]
    q.append(root)
    while(len(q)>0):
        print(q[0].data,end=" ")
        node=q.pop(0)
        if(node.left != None):
            q.append(node.left)
        if(node.right != None):
            q.append(node.right)
root= Node(1)
root.left=Node(2)
root.right=Node(4)
root.left.left=Node(3)
root.left.right=Node(6)   
root.right.left=Node(5)
root.right.right=Node(7)
levelordertraversal(root)