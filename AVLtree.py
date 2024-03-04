class Treenode:
    def __init__(self,key):
        self.key= key
        self.left = None
        self.right = None
        self.height = 1
        
class AVLtree:
    def __init__(self):
        self.root = None
        
    def insert(self,root,key):
        if not root:
            return Treenode(key)
        elif key < root.key:
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right, key)
            
        root.hight = 1 + max(self.getheight(root.left), self.getheight(root.right))
        balance = self.getbalance(root)         
        #left left case
        if balance > 1 and key > root.right.key:  
            return self.rightrotate(root)
        #right right case
        if balance < -1 and key > root.right.key:
            return self.leftrotate(root)
        #left right case
        if balance > 1 and key > root.left.key:
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)
        #right left case
        if balance < -1 and key < root.right.key:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)       
        return root
    def leftrotate(self,a):
        y = a.right
        T2 = y.left
        y.left = a
        a.right = T2
        a.hight = 1 + max(self.getheight(a.left), self.getheight(a.right))
        y.height = 1 + max(self.getheight(y.left), self.getheight(y.right))
        
        return y
    
    def rightrotate(self, y):
        x = y.left
        T2 = x.right 
        x.right = y
        y.left = T2
        y.height = 1+ max(self.getheight(y.left), self.getheight(y.right))
        x.height = 1+ max(self.getheight(x.left), self.getheight(x.right))
        
        return x
    
    def getheight(self, root):
        if not root:
            return 0
        return root.height
    
    def getbalance(self, root):
        if not root:
            return 0
        return self.getheight(root.left) - self.getheight(root.right)
    
    def insertkey(self,key):
        self.root = self.insert(self.root, key)
        
    def preordertraversal(self,root):
        if root:
            print(root.key, end=" ")
            self.preordertraversal(root.left)
            self.preordertraversal(root.right)
            
numbers = [50,45,55,35,40,48,60,20,70,41,47,42,15,22,25,30,90]

avl_tree = AVLtree()
for num in numbers:
    avl_tree.insertkey(num)
    
print("AVL tree is:")
avl_tree.preordertraversal(avl_tree.root)                