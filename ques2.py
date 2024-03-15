def coin_game_strategy(coins):
    # Calculate the sum of coins in the first and second halves
    sum_first_half = sum(coins[:len(coins)//2])
    sum_second_half = sum(coins[len(coins)//2:])
    
    # First player always chooses the half with the larger sum of coins
    if sum_first_half > sum_second_half:
        return "First player wins."
    elif sum_first_half < sum_second_half:
        return "Second player wins."
    else:
        return "It's a draw. First player can choose either half."

# Test case
coins = [18, 20, 15, 30, 10, 14]
print(coin_game_strategy(coins))
