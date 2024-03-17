
class Node:
  def __init__(self,data):
    self.left=None
    self.right=None
    self.data=data
  def printNode(self):
    print(self.data)
root=Node(10)
root.printNode()








class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

def printPreOrder(root):
  if root==None:
    return
  print(root.data,end=" ")
  printPreOrder(root.left)
  printPreOrder(root.right)

def printInOrder(root):
  if root==None:
    return
  printInOrder(root.left)
  print(root.data,end=" ")
  printInOrder(root.right)

def printPostOrder(root):
  if root==None:
    return
  printPostOrder(root.left)
  printPostOrder(root.right)
  print(root.data,end=" ")








if __name__=='__main__':
  root=Node(10)
  root.left=Node(20)
  root.right=Node(30)
  root.left.left=Node(40)
  root.left.right=Node(50)
  root.right.left=Node(60)
  root.right.right=Node(70)
  printPreOrder(root)
  print()
  printInOrder(root)
  print()
  printPostOrder(root)

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
        print()


root=node(1)
root.left=node(2)
root.right=node(4)
root.left.left=node(19)
root.left.right=node(14)
root.right.left=node(6)
root.right.right=node(12)
root.left.right.left=node(9)
root.left.right.right=node(5)
root.left.right.left.right=node(10)
root.right.left.right=node(16)
root.right.right.left=node(8)
root.right.right.right=node(11)
root.right.right.left.left=node(15)
root.right.right.right.left=node(17)
root.right.right.right.right=node(20)

print(root)
print(root.data)


print("Level order Traversal")
levelorder(root)
