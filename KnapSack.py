#0/1 Knapsack
items=[0, 1, 2, 3, 4, 5, 6]
price=[10, 5, 15, 7, 6, 18, 3]
weight=[2, 3, 5, 7, 1, 4, 1]
capacity=15
n=len(items)
ratios={}
for i in range(n):
    ratio = price[i] / weight[i]
    ratios[i] = ratio
sorted= sorted(ratios, key=ratios.get, reverse=True)
max=0
item=[]
for i in sorted:
    if weight[i] <= capacity:
        max += price[i]
        item.append(items[i])
        capacity -= weight[i]
print(f"Maximum value:{max}")
print(f"items:{item}")
