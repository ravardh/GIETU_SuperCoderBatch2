def max_Profit(length,price):
    N=len(length)
    ratio = [(price[i] / length[i], length[i], price[i]) for i in range(N)]
    ratio.sort(reverse=True)
    
    total_profit = 0.0
    remaining_weight = length[N-1]
    
    for i in range(N):
        if ratio[i][1] <= remaining_weight:
            total_profit += ratio[i][2]
            remaining_weight -= ratio[i][1]
    return total_profit

length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]

ans=max_Profit(length,price)
print(ans)


length2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
price2 = [3, 5, 8, 9, 10, 17, 17, 20, 22, 25, 30, 35]
print(max_Profit(length2,price2))