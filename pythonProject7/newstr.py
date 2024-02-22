str = "ABCBBACBAABACBABC"
pat = input("Enter the pattern: ")
index_length = []
for i in range(len(str) - (len(pat) - 1)):
    if str[i:i + len(pat)] == (pat):
        index_length.append(i)
print(index_length)
