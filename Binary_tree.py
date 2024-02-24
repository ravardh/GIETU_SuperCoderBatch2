class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def pre_order(root, lst):
    if root is None:
        return
    lst.append(root.data)
    pre_order(root.left, lst)
    pre_order(root.right, lst)

def in_order(root, lst):
    if root is None:
        return
    in_order(root.left, lst)
    lst.append(root.data)
    in_order(root.right, lst)

def post_order(root, lst):
    if root is None:
        return
    post_order(root.left, lst)
    post_order(root.right, lst)
    lst.append(root.data)

def level_order(root):
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

        

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(19)
root.left.right = TreeNode(14)
root.right.left = TreeNode(6)
root.right.right = TreeNode(12)
root.left.right.left=TreeNode(9)
root.left.right.right=TreeNode(5)
root.right.left.right=TreeNode(16)
root.left.right.left.right=TreeNode(10)
root.right.right.left=TreeNode(8)
root.right.right.right=TreeNode(11)
root.right.right.right.left=TreeNode(17)
root.right.right.right.right=TreeNode(20)




pre_list = []
pre_order(root, pre_list)
print("Pre-order:", pre_list)

post_list = []
post_order(root, post_list)
print("Post-order:", post_list)

in_list = []
in_order(root, in_list)
print("In-order:", in_list)

level_order(root)
