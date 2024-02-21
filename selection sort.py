#selection sort
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
n = len(my_list)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if my_list[j] < my_list[min_index]:
            min_index = j
    my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
print(my_list)
