class node:
  def _init_(self,data=None):
    self.data=data
    self.left=None
    self.right=None
def pre(root):
  if(root==None):
    #print("-1")
    return
  else:
    print(root.data)
    pre(root.left)
    pre(root.right)
root=node(1)
root.left=node(2)
root.right=node(4)
root.left.left=node(3)
root.left.right=node(6)
root.right.left=node(5)
root.right.right=node(7)
pre(root)