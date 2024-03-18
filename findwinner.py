class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


def find_winner(N, K):

    head = Node(1)
    prev = head
    for i in range(2, N + 1):
        prev.next = Node(i)
        prev = prev.next
    prev.next = head 
    current = head
    while current.next != current:

        for _ in range(K - 1):
            current = current.next

        current.data = current.next.data
        current.next = current.next.next

    return current.data

N = 14
K = 20
print("The winning child is:", find_winner(N, K))