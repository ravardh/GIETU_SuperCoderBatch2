class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.key = None
        
def topView(node):
    if(node == None):
        return
    Q=[node]
    key=0
    TView=dict()
    node.key=key
    while len(Q) !=0:
        cur = Q.pop(0)
        key = cur.key
        if key not in TView:
            TView[key]=cur.data
            
        if cur.left != None:
            Q.append(cur.left)
            cur.left.key=key-1
            
        if cur.right != None:
            Q.append(cur.right)
            cur.right.key=key+1
            
    for x in sorted(TView.keys()):
        print(TView[x],end=" ")
      
'''
         1
       /   \
      2     4
     / \   / \
    3   6  5  7
'''
root = Node(1)

root.left = Node(2)
root.right= Node(4)

root.left.left = Node(3)
root.left.right = Node(6)

root.right.right= Node(7)
root.right.left= Node(5)

print("Nodes at the topview are:")
topView(root)
