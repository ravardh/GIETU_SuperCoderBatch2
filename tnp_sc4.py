# -*- coding: utf-8 -*-
"""TNP_SC4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cpISyugtgDtJxprqS_tdgvpjzNHFGG-e
"""

class Node:
  def __init__(self,data):
    self.left=None
    self.right=None
    self.data=data


'''def insert(self,data):
    if self.data:
      if data<self.data:
        if self.left==None:
          self.left=Node(data)
        else:
          self.left.insert(data)
      elif data>self.data:
        if self.right==None:
          self.right=Node(data)
        else:
          self.right.insert(data)
    else:
      self.data=data
'''
def PrintTree(self):
    if self.left:
      self.left.PrintTree()
    print( self.data)
    if self.right:
      self.right.PrintTree()

def InOrder(root):
  if(root==None):
    return
  InOrder(root.left)
  print(root.data)
  InOrder(root.right)


def PreOrder(root):
  if(root==None):
    return
  print(root.data)
  PreOrder(root.left)
  PreOrder(root.right)


def PostOrder(root):
  if(root==None):
    return
  PostOrder(root.left)
  PostOrder(root.right)
  print(root.data)

if __name__=='__main__':
  root=Node(10)
  root.left=Node(20)
  root.right=Node(30)
  root.left.left=Node(40)
  root.left.right=Node(50)
  root.right.left=Node(60)
  root.right.right=Node(70)
  #root.PrintTree()
  print(root)
  print(root.data)

  print("Inorder traversal")
  InOrder(root)

  print("Preorder traversal")
  PreOrder(root)

  print("Postorder traversal")
  PostOrder(root)
'''
print(root)
print(root.data)

print("Inorder traversal")
InOrder(root)

print("Preorder traversal")
PreOrder(root)

print("Postorder traversal")
PostOrder(root)
'''

from collections import deque as queue

class Node:

	def __init__(self, key):

		self.data = key
		self.left = None
		self.right = None

def levelOrder(root):

	if (root == None):
		return
	q = queue()

	q.append(root)
	q.append(None)

	while (len(q) > 1):
		curr = q.popleft()
		# q.pop()
		if (curr == None):
			q.append(None)
			print()

		else:
			if (curr.left):
				q.append(curr.left)

			if (curr.right):
				q.append(curr.right)

			print(curr.data, end=" ")
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(6)

	levelOrder(root)