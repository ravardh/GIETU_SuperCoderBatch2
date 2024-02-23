# Exception Handling
x = input()
try:
    for i in range(1,11):
        print(f'{int(x)} X {int(i)} = {int(x) * i}')
except:
    print('Invalid Input')


# Sliding Window Maximum
arr = list(map(int, input("Enter an array: ").split()))
k = int(input("Enter the window size: "))
max_sum = float('-inf')
for i in range(len(arr) - k + 1):
    current_sum = sum(arr[i:i+k])
    max_sum = max(max_sum, current_sum)
print(f'The maximum sum of {k} consecutive numbers is {max_sum}')

# String Matching
def kmp(s, p):
    m, n = len(s), len(p)
    for i in range(m - n + 1):
         if s[i:i+n] == p:
            print(f"Pattern found at index {i}")
            return
    print("Pattern not found")

string = input("Enter the string: ")
pattern = input("Enter the pattern: ")
kmp(string, pattern)