my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
n = len(my_list)
for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print(my_list)