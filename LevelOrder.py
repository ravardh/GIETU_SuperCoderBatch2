class TreeNode:
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None
def LevelOrder(root):
    queue = []
    queue.append(root)
    while queue:
        cur = queue.pop(0)
        if cur:
            print(cur.data, end=" ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        elif queue:
            queue.append(None)


root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

LevelOrder(root)

