class node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def inorder(root):
    if(root):
        preorder(root.left)
        print(root.val)
        preorder(root.right)

def preorder(root):
    if(root):
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if(root):
        preorder(root.left)
        preorder(root.right)
        print(root.val)

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
root.right=node(3)
root.left.left=node(3)
root.left.right=node(6)
root.right.left=node(5)
root.right.right=node(7)

print(root)
print("inorder traversal: ")
inorder(root)
print("preorder traversal: ")
preorder(root)
print("postorder traversal: ")
postorder(root)
print("levelorder traversal: ")
levelorder(root)