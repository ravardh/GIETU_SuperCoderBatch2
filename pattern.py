str = "ABCBBACBAABACBABC"
p = input("enter the patterns:")
index_length = []
for i in range(len(str)-(len(p)-1)):
    if str[i:i +len(p)] == (p):
        index_length.append(i)
print(index_length)