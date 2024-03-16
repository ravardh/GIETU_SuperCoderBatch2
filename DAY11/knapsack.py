price=[10,5,15,7,6,18,3]
weight=[2,3,5,7,1,4,1]
max=15
n=7
def knapsack(weight,price,n,max):
    if(n==0 or max==0):
        return 0
    elif(weight[n-1]<=max):
        return max(price[n-1]+knapsack(weight,price,max-weight[n-1],n-1),knapsack(weight,price,max,n-1))
    elif(weight[n-1]>max):
        return knapsack(weight,price,n,max)
knapsack(weight,price,n,max)




