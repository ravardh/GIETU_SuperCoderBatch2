class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def print(self):
        print(self.data)
root=node(7)
root.left=node(2)
root.right=node(4)

print(root)
print(root.data)

