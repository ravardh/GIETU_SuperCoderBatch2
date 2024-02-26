from tree.Tree import Node


def level_order(root: Node | None):
    queue: list = [root, None]

    while len(queue) != 0:
        currNode: Node | None = queue[0]
        if currNode is None:
            queue.remove(currNode)
            print()
            if len(queue) == 0:
                return
            else:
                queue.append(None)
            currNode = queue[0]

        print(queue[0].data, end="   ")

        if currNode.has_left():
            queue.append(currNode.left)

        if currNode.has_right():
            queue.append(currNode.right)

        queue.remove(currNode)


if __name__ == '__main__':
    root: Node = Node("1")
    root.left = Node("2")
    root.right = Node("4")
    root.left.left = Node("19")
    root.left.right = Node("14")
    root.right.left = Node("6")
    root.right.right = Node("12")
    root.left.right.left = Node("9")
    root.left.right.right = Node("5")
    root.right.left.right = Node("16")
    root.right.right.left = Node("8")
    root.right.right.right = Node("11")
    root.left.right.left.right = Node("10")
    root.right.right.left.left = Node("15")
    root.right.right.right.left = Node("17")
    root.right.right.right.right = Node("20")
    level_order(root)
