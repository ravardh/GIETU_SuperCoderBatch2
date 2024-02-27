class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.key = 0
def Bottom_view(root):
    if(root == None):
        return
    q = [root]
    key = 0
    Bview = dict()
    root.key = key
    while len(q) != 0:
        curr = q.pop(0)
        key = curr.key
        Bview[key] = curr.data
        if curr.left != None:
            q.append(curr.left)
            curr.left.key = key-1
        if curr.right != None:
            q.append(curr.right)
            curr.right.key = key+1
    for x in sorted(Bview.keys()):
        print(Bview[x], end=" ")

if __name__ == '__main__':
    root = node(20)
    root.left = node(32)
    root.right = node(10)
    root.left.left = node(15)
    root.left.right = node(7)
    root.right.left = node(4)
    root.right.right = node(6)
    root.left.left.right = node(8)

Bottom_view(root)