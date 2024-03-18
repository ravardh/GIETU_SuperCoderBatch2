def first_player_wins(coins):
    if len(coins) % 2 != 0:
        return "Invalid input: Number of coins must be even"

    first_player_sum = 0
    second_player_sum = 0

    while coins:
        if coins[0] > coins[-1]:
            first_player_sum += coins.pop(0)
        else:
            first_player_sum += coins.pop()

        if coins[0] > coins[-1]:
            second_player_sum += coins.pop(0)
        else:
            second_player_sum += coins.pop()

    if first_player_sum > second_player_sum:
        return "First player wins."
    else:
        return "Second player wins."

coins = [18, 20, 15, 30, 10, 14]
print(first_player_wins(coins))
