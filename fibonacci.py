def fibonachi(num: int, dp: list) -> int:
    if num == 0 or num == 1:
        dp[num] = num
        return num
    if dp[num] != -1:
        return dp[num]
    dp[num] = fibonachi(num - 1, dp) + fibonachi(num - 2, dp)
    return dp[num]


if __name__ == '__main__':
    n: int = 7
    dp_arr: list = []
    for i in range(n + 1):
        dp_arr.append(-1)
    # print(dp_arr)

    print(fibonachi(n, dp_arr))