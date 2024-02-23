#!/usr/bin/env python
# coding: utf-8

# # Quick Sort

# In[20]:


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])


    (array[i + 1], array[high]) = (array[high], array[i + 1])


    return i + 1

def quicksort(array, low, high):
    if low < high:


        pi = partition(array, low, high)


        quicksort(array, low, pi - 1)


        quicksort(array, pi + 1, high)



        

if __name__ == '__main__':
    array = [1,5,8,2,9,4,9,2]
    N = len(array)

    quicksort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")



# # Merge Sort
# 

# In[1]:


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]  
        right_half = arr[mid:]

        merge_sort(left_half)  
        merge_sort(right_half)  

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array:", arr) 


# # calculator

# In[2]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error"
    return x / y

def calculator(operator, x, y):
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    operation = operations.get(operator)
    if operation:
        return operation(x, y)
    else:
        return "Invalid operator"

operator = input("Enter the operator (add, subtract, multiply, divide): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculator(operator, num1, num2)
print("Result:", result)


# In[ ]:




