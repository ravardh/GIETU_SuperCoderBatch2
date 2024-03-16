def coin_game_strategy(coins):
    sum_odd_indices = sum(coins[i] for i in range(0, len(coins), 2))
    sum_even_indices = sum(coins[i] for i in range(1, len(coins), 2))
    start_from_left = sum_odd_indices >= sum_even_indices
    first_player_total = 0
    second_player_total = 0
    left, right = 0, len(coins) - 1
    while left <= right:
        if start_from_left:
            if coins[left] >= coins[right]:
                first_player_total += coins[left]
                left += 1
            else:
                first_player_total += coins[right]
                right -= 1
        else:
            if coins[right] >= coins[left]:
                first_player_total += coins[right]
                right -= 1
            else:
                first_player_total += coins[left]
                left += 1
        if left <= right:
            if coins[left] >= coins[right]:
                second_player_total += coins[left]
                left += 1
            else:
                second_player_total += coins[right]
                right -= 1
    if first_player_total > second_player_total:
        return "First player wins."
    elif first_player_total < second_player_total:
        return "Second player wins."
    else:
        return "It's a tie."
coins = [18, 20, 15, 30, 10, 14]
print(coin_game_strategy(coins))
