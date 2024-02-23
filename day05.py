# String Searching using KMP algorithm
def KMPSearch(pat, data):
	M = len(pat)
	N = len(data)
	
	lps = [0]*M
	j = 0 
	
	LPS(pat, M, lps)

	i = 0 
	while (N - i) >= (M - j):
		if pat[j] == data[i]:
			i += 1
			j += 1

		if j == M:
			print("Found pattern at index " + str(i-j))
			j = lps[j-1]

		elif i < N and pat[j] != data[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1



def LPS(pat, M, lps):
	len = 0 

	lps[0] = 0 
	i = 1

	
	while i < M:
		if pat[i] == pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[len-1]
			else:
				lps[i] = 0
				i += 1


if __name__ == '__main__':
	data = "ABAABABCABABABCAABABCABAC"
	pat = "ABABC"
	KMPSearch(pat, data)


# Linked List
class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

def insert_at_head(head, data):
	new_node = ListNode(data)
	new_node.next = head
	return new_node

def insert_at_position(head, data, position):
    if position == 0:
        return insert_at_head(head, data)
	
    new_node = ListNode(data)
    temp = head
    for _ in range(position - 1):
        if not temp:
            print("Invalid position")
            return head
        temp = temp.next
    new_node.next = temp.next
    temp.next = new_node

    return head

def insert_at_tail(head, data):
    new_node = ListNode(data)
    if not head:
        return new_node
	
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node

    return head

def display(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


head = None
while True:
	print("\n1. Insert at Head")
	print("2. Insert at Tail")
	print("3. Insert at Position")
	print("4. Display")
	print("5. Exit")
    
	choice = int(input("Enter your choice: "))
	match choice:
		case 1:
			data = int(input("Enter data: "))
			head = insert_at_head(head, data)
		case 2:
			data = int(input("Enter data: "))
			head = insert_at_tail(head, data)
		case 3:
			data = int(input("Enter data: "))
			position = int(input("Enter position: "))
			head = insert_at_position(head, data, position)
		case 4:
			display(head)
		case 5:
			break
		case _:
			print("Invalid choice. Try again.")


# Recursion
def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n - 1)
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")