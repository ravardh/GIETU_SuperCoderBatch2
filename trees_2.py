def findHeight(root):
     if root == None:
          return 0
     return max(findHeight(root.left),findHeight(root.right))+1

def printLeaf(root):
     if root==None:
          return 0
     elif root.left==None and root.right==None:
          print(root.data, end=" ")
     printLeaf(root.left)
     printLeaf(root.right)

def topView(root):
     if root==None:
          return
     Q=[root]
     key=0
     tview = dict()
     root.key=key
     while len(Q)!=0:
          curr = Q.pop(0)
          key=curr.key
          if key not in tview:
               tview[key]=curr.data
          if curr.left!=None:
               Q.append(curr.left)
               curr.left.key = key-1
          if curr.right!=None:
               Q.append(curr.right)
               curr.right.key=key+1
     for x in sorted(tview.keys()):
          print(tview[x],end=" ")

def bottomView(root):
     if root==None:
          return
     Q=[root]
     key=0
     bview = dict()
     root.key=key
     while len(Q)!=0:
          curr = Q.pop(0)
          key=curr.key
          bview[key]=curr.data
          if curr.left!=None:
               Q.append(curr.left)
               curr.left.key = key-1
          if curr.right!=None:
               Q.append(curr.right)
               curr.right.key=key+1
     for x in sorted(bview.keys()):
          print(bview[x],end=" ")