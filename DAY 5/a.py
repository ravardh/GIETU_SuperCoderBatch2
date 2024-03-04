class node:
    def _init_(self,data):
        self.left=None
        self.data=data
        self.right=None
def findheight(root):

    if root==None:
        return 0
    height=max(findheight(root.left),findheight(root.right))+1
    return height

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
print(findheight(root))