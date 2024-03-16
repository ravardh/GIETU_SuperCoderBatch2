#max profit

def max_Profit(capacity, weights, prices):
    n = len(prices)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                table[i][w] = max(prices[i - 1] + table[i - 1][w - weights[i - 1]], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]

    maxValue = table[n][capacity]
    return maxValue

w = int(input("Enter the total weight (limited) of the products to carry: "))
n = int(input("Total no. of products to choose from : "))
i=0
pp = []
pw = []
while i<n:
    a = int(input("Enter wright :"))
    pw.append(a)
    b = int(input("Enter profit : "))
    pp.append(b)
    i=i+1
maxProfit = max_Profit(w, pw, pp)
print("Maximum value:", maxProfit)