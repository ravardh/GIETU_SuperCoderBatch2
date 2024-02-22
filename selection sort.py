#selection sort
l = list(eval(input("Enter a list: ")))
for i in range(len(l)):
    pos = i
    for j in range(i + 1, len(l)):
        if l[j] < l[pos]:
            pos = j
    l[i],l[pos] = l[pos], l[i]
print(l)