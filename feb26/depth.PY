class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


root = node(1)
root.left = node(2)
root.right = node(4)
root.left.left = node(3)
root.left.right = node(6)
root.right.left = node(5)
root.right.right = node(7)
# print(root)

#         1
#     2       4
#   3   6   5   7


def height_tree(node):
    if node is None:
        return 0
    # return max(height_tree(node.left), height_tree(node.right))+1
    else:
        left = height_tree(node.left)
        right = height_tree(node.right)

        height = max(left, right) + 1

    return height


print(height_tree(root))


def leaf_Node(node):
    if node is None:
        return 0

    if node.left == None and node.right == None:
        print(node.data)
        return

    leaf_Node(node.left)
    leaf_Node(node.right)


print(leaf_Node(root))
#         1
#     2       4
#   3   6   5   7

3
