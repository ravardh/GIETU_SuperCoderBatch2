class TreeNode:
    def _init_(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.hd = 0  # Horizontal distance

def top_view(root):
    if root == None:
        return 0

    queue = []
    top_view_nodes = {}

    queue.append(root)

    while queue:
        temp = queue[0]
        queue.pop(0)
        hd = temp.hd
        if hd not in top_view_nodes:
            top_view_nodes[hd] = temp.key
        if temp.left:
            temp.left.hd = hd - 1
            queue.append(temp.left)

        if temp.right:
            temp.right.hd = hd + 1
            queue.append(temp.right)

    for key in sorted(top_view_nodes.keys()):
        print(top_view_nodes[key], end=" ")

if _name_ == "_main_":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)
    root.left.right.right.right = TreeNode(6)

    print("Top view of the binary tree is:", end=" ")
    top_view(root)