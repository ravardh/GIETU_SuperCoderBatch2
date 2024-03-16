def optimalStrategy(coins):
    n = len(coins)
    evenSum = sum(coins[i] for i in range(0, n, 2))
    oddSum = sum(coins[i] for i in range(1, n, 2))
    if evenSum >= oddSum:
        return "First player wins."
    else:
        return "Second player wins."
try:
    coins = list(map(int, input("Enter the values of coins separated by space: ").split()))
    if len(coins) % 2 != 0:
        raise ValueError("Number of coins must be even.")
    print(optimalStrategy(coins))
except ValueError as ve:
    print("Error:", ve)
