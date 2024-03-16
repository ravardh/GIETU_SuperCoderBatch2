# One day, Peter and his wife Linda moved to a grocery market to buy some groceries and other items. They only picked up the items those were having some discounts but their little son Carl picked up some toys he liked most. Later at the billing counter, Peter found that the bill was too high than expected and there were so many products to carry that they can’t. Finally, they decided to select and buy the items with a limited weight ‘W’ but wanted to keep most of items with great profit even by picking the product in the fractions. Would you please help them by implementing a logic for selecting the maximum no. of items within the total carry weight of ‘W’?  
# Inputs are as given below;
# First line input - W: The total weight (limited) of the products to carry
# Second line input - N: Total no. of products to choose from
# Third line inputs - PW[N] : Weight of each product
# Fourth line inputs - PP[N] : Profit from each product
# TEST CASE 	
# INPUT
# W: 15
# N: 4
# PW[4]: 5 10 10 5
# PP[4]: 10 5 5 10
# OUTPUT
# Max Profit: 22.5
def knapsack(W,N,PW,PP):
    i=[(PP[i]/PW[i],PW[i],PP[i])for i in range(N)]
    i.sort(reverse=True)
    total=0
    current_weight=0
    for profit_density,weight,profit in i:
        if current_weight+weight<=W:
            total +=profit
            current_weight+=weight
        else:
            remaining_weight=W-current_weight
            total+=profit_density*remaining_weight
            break
    return total
W=15
N=4
PW=[5, 10, 10, 5]
PP=[10, 5, 5, 10]
max_profit=knapsack(W,N,PW,PP)
print("Max Profit:",max_profit)
