# LINK LIST
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

newNode = node(1)
start = newNode

start.next = node(2)
start.next.next = node(3)
start.next.next.next = node(4)
start.next.next.next.next = node(5)

temp = start
# print(temp)
while temp:
    print(temp.data)
    temp = temp.next


n1 = node(0)
n1.next = start
start = n1
print("Node added into begining")

temp = start
# print(temp)
while temp:
    print(temp.data)
    temp = temp.next


n2 = node(6)
temp = start
while temp.next:
    temp = temp.next
temp.next = n2
print("Node added into End")

temp = start
# print(temp)
while temp:
    print(temp.data)
    temp = temp.next


#Power using recursion
def power(x, n):
    if n == 0:
        return 1
    return (x*power(x, n-1))


x = int(input("enter the base: "))
n = int(input("enter the exponent: "))
print(power(x, n))



# KMP
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

data = "ABAABABCABABABCAABABCABAC"
pat = "ABA"
KMPSearch(pat, data)


#Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return (n*factorial(n-1))

n=int(input("enter a number: "))
print(factorial(n))