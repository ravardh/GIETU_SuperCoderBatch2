def bubble(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j+1],array[j]=array[j],array[j+1]
    return array
array = [40,30,20,10]
sortedarr = bubble(array)
print(sortedarr)

