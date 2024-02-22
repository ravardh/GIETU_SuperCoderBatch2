arr = "ABCBBACBAABACBABC"

pat = input("Enter your pattern:")
index_list=[]

for i in range(len(arr)-(len(pat)-1)):
    if arr[i:i+len(pat)]==pat:
        index_list.append(i)

print(index_list)