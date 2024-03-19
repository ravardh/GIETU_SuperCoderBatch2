def knapsack0_1(bag_capacity,weights,price):
    n=len(price)
    knapsack={}

    for i in range(n):
        if type(price[i]/weights[i])==float:
            knapsack[i]=round((price[i]/weights[i]), 2)
        else:
            knapsack[i]=price[i]/weights[i]
    sorted_knapsack=sorted(knapsack.items(),key=lambda item: item[1],reverse=True)
    
    max_profit=0
    for key,value in sorted_knapsack:
        if weights[key]<=bag_capacity:
            max_profit=max_profit+price[key]
            #print(bag_capacity,key)
            bag_capacity=bag_capacity-weights[key]
    print("Max Profit:",max_profit)

bag_capacity=15
weights=[2, 3, 5, 7, 1, 4, 1]
price = [10, 5, 15, 7, 6, 18, 3]

knapsack0_1(bag_capacity,weights,price)