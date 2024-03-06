if __name__ == '__main__':
    items: list = [0, 1, 2, 3, 4, 5, 6]
    price: list = [10, 5, 15, 7, 6, 18, 3]
    weight: list = [2, 3, 5, 7, 1, 4, 1]
    capacity: int = 15

    dp: list = []
    for i in range(len(items) + 1):
        arr: list = []
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                arr.append(0)

        dp.append(arr)

    for i in dp:
        print(i)

    for i in range(1, len(dp)):
        for j in range(1, 16):
            if j - weight[i - 1] < 0:
                max_val = dp[i - 1][j]
            else:
                max_val: int = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + price[i - 1])
            dp[i].append(max_val)

    for i in dp:
        print(i)

    print(dp[len(items)][capacity])
