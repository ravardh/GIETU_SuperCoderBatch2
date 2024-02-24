
class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
        
def preorder(root):
    #print(root)
    if(root != None):
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if(root != None):
        print(root.data)
        postorder(root.right)
        postorder(root.left)
        

if __name__ == "__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(4)
    root.left.left=node(6)
    root.left.right=node(7)
    root.right.left=node(5)
    root.right.right=node(9)
    print("P R E O R D E R ")
    preorder(root)
    print("P O S T O R D E R ")
    postorder(root)