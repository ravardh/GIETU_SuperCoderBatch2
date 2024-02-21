#insertion sort
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
for i in range(1, len(my_list)):
    current_element = my_list[i]
    j = i - 1

    while j >= 0 and current_element < my_list[j]:
        my_list[j + 1] = my_list[j]
        j -= 1
    my_list[j + 1] = current_element
print(my_list)