class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def preorder(root):
        if root == None:
            return 
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
     if root == None:
          return
     inorder(root.left)
     inorder(root.right)
     print(root.data)

def postorder(root):
     if root == None:
          return
     postorder(root.right)
     postorder(root.left)
     print(root.data)

def levelOrder(root):
    if root is None:
        return
    
    q = []
    q.append(root)

    while q:
        level_length = len(q)
        for i in range(level_length):
            current = q.pop(0)
            print(current.data, end=" ")
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        print()  # Move to the next level


     


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.right = Node(3)
    root.right = Node(4)
    # print("preorder")
    # print(preorder(root))
    # print("inorder")
    # print(inorder(root))
    # print("Postoder")
    # print(postorder(root))
    print("Level order")
    print(levelOrder(root))

