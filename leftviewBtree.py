class Treenode:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def left_view(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        size = len(queue)
        
        for i in range(size):
            node = queue.pop(0)
            
            if i == 0:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return result

root =Treenode(1)
root.left = Treenode(5) 
root.right = Treenode(7)
root.left.left = Treenode(2)
root.left.right =  Treenode(11)
root.right.right = Treenode(17)
root.left.left.left = Treenode(20)
root.left.right.left = Treenode(11)
root.left.right.right = Treenode(3)
root.right.right.left =  Treenode(12)
root.right.right.right = Treenode(16)
root.left.left.left.right = Treenode(10)
root.right.right.left.left =  Treenode(14)
root.right.right.left.right = Treenode(19)
root.left.left.left.right.left = Treenode(21)
root.right.right.left.right.right = Treenode(18)
root.right.right.left.right.right.right = Treenode(15)

print("Left view of the binary tree:", left_view(root))                           