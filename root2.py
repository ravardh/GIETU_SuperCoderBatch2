class node:
  def _init_(self,data=None):
    self.data=data
    self.left=None
    self.right=None
def preorder(root):
  if(root==None):
    #print("-1")
    return
  else:
    print(root.data)
    preorder(root.left)
    preorder(root.right)
def inorder(root):
  if(root==None):
    return
  inorder(root.left)
  print(root.data)
  inorder(root.right)
def postorder(root):
  if(root==None):
    return
  postorder(root.left)
  postorder(root.right)
  print(root.data)
root=node(1)
root.left=node(2)
root.right=node(4)
root.left.left=node(3)
root.left.right=node(6)
root.right.left=node(5)
root.right.right=node(7)
print('The preoder series is :')
preorder(root)
print('The inoder series is :')
inorder(root)
print('The postoder series is :')
postorder(root)