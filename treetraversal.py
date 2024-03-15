class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):
    if root == None:
        return
    
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def preorder(root):
    if root == None:
        return
    
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

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
        print()  # Move the newline here to print after each level

def findDepth(root):
    if root == None:
        return 0
    return max(findDepth(root.left), findDepth(root.right)) + 1

def print_leaf_nodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data)

    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)

root = node(1)
root.left = node(2)
root.right = node(4)
root.left.left = node(19)
root.left.right = node(14)
root.right.left = node(6)
root.right.right = node(12)
root.left.right.left = node(9)
root.left.right.right = node(5)
root.left.right.left.right = node(10)
root.right.left.right = node(16)
root.right.right.left = node(8)
root.right.right.right = node(11)
root.right.right.left.left = node(15)
root.right.right.right.left = node(17)
root.right.right.right.right = node(20)


def topview(root):
  if(root==None):
    return
  Q=[root]
  keyd=0
  TView=dict()
  root.key=key

  while len(Q)!=0:
    curr=Q.pop(0)
    key=root.Key
    if key not in TView:
      TView[key]=root.data
    if curr.left!=None:
      Q.append(curr.left)
      curr.left.key=key-1
    if curr.right!=None:
      Q.append(curr.right)
      curr.left.key=key+1
  for x in sorted(TView.keys()):
    print(TView[x],end=" ")

print("Inorder traversal")
inorder(root)

print("Preorder traversal")
preorder(root)

print("Postorder traversal")
postorder(root)

print("Level order Traversal")
levelorder(root)

print("Height of the tree")
print(findDepth(root))
print_leaf_nodes(root)