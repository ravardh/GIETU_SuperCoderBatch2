#insertion sort
l = list(eval(input("Enter a list: ")))
for i in range(1, len(l)):
        val = l[i]
        j = i - 1
        while j >= 0 and val < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = val
print(l)