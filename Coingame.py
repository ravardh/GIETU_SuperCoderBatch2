def winning_strategy(coins):
    n = len(coins)
    if sum(coins[::2])>sum(coins[1::2]):
        return "First player wins."
    else:
        return "Second player wins."

coins = [18,20,15,30,10,14]
result = winning_strategy(coins)
print("Result:",result)