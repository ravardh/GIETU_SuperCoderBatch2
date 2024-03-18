#0/1 Knapsack
items=[0, 1, 2, 3, 4, 5, 6]
price=[10, 5, 15, 7, 6, 18, 3]
weight=[2, 3, 5, 7, 1, 4, 1]
capacity=15
rows =len(items)
columns =capacity+1
arr= [[0 for _ in range(columns)] for _ in range(rows)]
for i in range(1,rows):
    for w in range(1,columns):
            arr[i][w]=max(arr[i-1][w],arr[i-1][w-weight[i]]+price[i])
print("The maximum capacity is:-",arr[rows-1][columns-1])
