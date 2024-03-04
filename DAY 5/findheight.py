class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
def findheight(root):
    if root==None:
        return 0
    height=max(findheight(root.left),findheight(root.right))+1
    return height

def leafnodes(root):
    if root== None:
        return 
    elif(root.left==None and root.right==None):
        print(root.data)
    leafnodes(root.left)
    leafnodes(root.right)

def bottomview(root):
    if root ==None:
        return
    
    Q=[root]
    key=0
    Tview = dict()
    root.key=key 

    while len(Q) !=0:
        curr=Q.pop(0)
        key=curr.key
        
        Tview[key] = curr.data
        if curr.left != None:
            Q.append(curr.left)
            curr.left.key = key-1
        if curr.right != None:
            Q.append(curr.right)
            curr.right.key =key+1

    for x in sorted(Tview.keys()):
        print(Tview[x], end =" ")

def topview(root):
    if root ==None:
        return
    
    Q=[root]
    key=0
    Tview = dict()
    root.key=key 

    while len(Q) !=0:
        curr=Q.pop(0)
        key=curr.key
        if key not in Tview:
            Tview[key] = curr.data
        if curr.left != None:
            Q.append(curr.left)
            curr.left.key = key-1
        if curr.right != None:
            Q.append(curr.right)
            curr.right.key =key+1

    for x in sorted(Tview.keys()):
        print(Tview[x], end =" ")



root=node(20)
root.left=node(32)
root.right=node(10)
root.left.left=node(15)
root.left.right=node(12)
root.right.left=node(8)
root.right.right=node(24)
root.left.left.left=node(4)
root.left.right.left=node(50)
root.left.right.right=node(6)
root.left.right.left.left=node(40)
root.left.right.left.right=node(35)
root.right.right.left=node(16)
root.right.right.right=node(2)

#print("Print Max height",findheight(root))
#print("Print Leaf Nodes Are:-")
#leafnodes(root)
print("Top View :-")
topview(root,)
print()
print("Bottom View :-")
print(bottomview(root))