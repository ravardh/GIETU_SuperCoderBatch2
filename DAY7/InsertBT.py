class node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

def insert(root,value):
    if value<root.data:
        if root.left == None:
            root.left = node(value)
            return
        insert(root.left,value)
        
    elif value>root.data:
        if root.right == None:
            root.right = node(value)
            return
        insert(root.right,value)
        

def preorder(root):
    if root == None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


V_L = [50,36,12,20,44,76,18,44,52,90]
root = node(V_L[0])
for x in range(1,len(V_L)):
    insert(root,V_L[x])

print(root)
preorder(root)