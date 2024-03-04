
#Height of a binary tree
class node:
  def __init__(x, data):
        x.data = data
        x.left = None
        x.right = None
def height(root):
  if(root==None):
   return 0;
  return max(height(root.left),height(root.right))+1
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
root.left.left.right=node(8)
root.left.left.left=node(9)
root.left.left.right.left=node(10)
root.left.left.right.right=node(11)
print(height(root))
height(root)