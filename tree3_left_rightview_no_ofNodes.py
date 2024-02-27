def leftViewUtil(root,max_level,level):
     if root == None:
          return 
     if max_level[0] < level:
          print(root.data,end=" ")
          max_level[0]=level
     
     leftViewUtil(root.left,max_level,level+1)
     leftViewUtil(root.right,max_level,level+1)

def leftView(root):
     max_level = [0]
     leftViewUtil(root,max_level,1)


def rightViewUtil(root,max_level,level):
     if root == None:
          return 
     if max_level[0] < level:
          print(root.data,end=" ")
          max_level[0]=level
     
     leftViewUtil(root.right,max_level,level+1)
     leftViewUtil(root.left,max_level,level+1)

def rightView(root):
     max_level = [0]
     rightViewUtil(root,max_level,1)

def numberOfNode(root):
     if root==None:
          return 0
     return 1+numberOfNode(root.left)+numberOfNode(root.right)