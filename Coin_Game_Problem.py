def coin_game_strategy(coins):
    total_coins = len(coins)
    if total_coins % 2 != 0:
        return "Invalid input: Number of coins should be even"

    def max_value(coins, start, end):
        if start == end:
            return coins[start]
        if start + 1 == end:
            return max(coins[start], coins[end])

        return max(
            coins[start] + min(max_value(coins, start + 2, end), max_value(coins, start + 1, end - 1)),
            coins[end] + min(max_value(coins, start + 1, end - 1), max_value(coins, start, end - 2))
        )

    max_value_second_player = max_value(coins, 0, total_coins - 1)
    total_value = sum(coins)
    if max_value_second_player > total_value - max_value_second_player:
        return "Second player wins"
    elif max_value_second_player == total_value - max_value_second_player:
        return "The game is a tie"
    else:
        return "First player wins"

coins = [18, 20, 15, 30, 10, 14]
print(coin_game_strategy(coins))
