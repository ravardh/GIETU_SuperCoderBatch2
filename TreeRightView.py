class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def right_View(root,level,max):
    if root is None:
        return
    if(max[0]<level):
        print(root.data,end=" ")
        max[0] = level
        right_View(root.right, level+1, max)
        right_View(root.left, level+1, max)
def RightView(root):
        max = [0]
        right_View(root,1,max)

if __name__ == '__main__':
    root = node(20)
    root.left = node(32)
    root.right = node(10)
    root.left.left = node(15)
    root.left.right = node(7)
    root.right.left = node(4)
    root.right.right = node(6)
    root.left.left.right = node(8)

    print(RightView(root))