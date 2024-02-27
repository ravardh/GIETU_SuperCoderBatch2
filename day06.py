# Trees
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def build_tree():
    root_val = int(input("Enter the value for the current(root) node: "))
    root = TreeNode(root_val)
    queue_of_nodes = [root]

    while queue_of_nodes:
        current_node = queue_of_nodes.pop(0),

        left_val = input(f"Enter the value for the left child of {current_node.val} (or press Enter for None): ")
        if left_val:
            current_node.left = TreeNode(int(left_val))
            queue_of_nodes.append(current_node.left)

        right_val = input(f"Enter the value for the right child of {current_node.val} (or press Enter for None): ")
        if right_val:
            current_node.right = TreeNode(int(right_val))
            queue_of_nodes.append(current_node.right)
        
    return root

def preorder(root):
    '''Preorder Traversal'''
    if not root:
        return
    print(root.val, end = '->')
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    '''Inorder Traversal'''
    if not root:
        return
    inorder(root.left)
    print(root.val, end = '->')
    inorder(root.right)

def postorder(root):
    '''Postorder Traversal'''
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end = '->')

def levelorder(root):
    '''Levelorder Traversal'''
    if not root:
        return
    queue_of_nodes = [root]
    while queue_of_nodes:
        current_node = queue_of_nodes.pop(0)
        print(current_node.val, end = '->')
        if current_node.left:
            queue_of_nodes.append(current_node.left)
        if current_node.right:
            queue_of_nodes.append(current_node.right)
        


if __name__ == '__main__':
    my_tree = build_tree()
    print("1. Preorder Traversal", "2. Inorder Traversal", "3. Postorder Traversal", "4. Levelorder Traversal", "5. Exit", sep = '\n')
    choice = int(input("Enter your choice: "))
    while True:
        match choice:
            case 1: preorder(my_tree)
            case 2: inorder(my_tree)
            case 3: postorder(my_tree)
            case 4: levelorder(my_tree)
            case 5: break
            case _: print("Enter a valid choice.")