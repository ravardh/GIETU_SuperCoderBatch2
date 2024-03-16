def coin_game_strategy(coins):
    if coins[0] > coins[-1]:
        first_player_total = coins[0]
        second_player_total = coins[-1]
        coins = coins[1:] 
    else:
        first_player_total = coins[-1]
        second_player_total = coins[0]
        coins = coins[:-1] 
    
    while len(coins) > 0:
        if coins[0] > coins[-1]:
            second_player_total += coins[0]
            coins = coins[1:]
        else:
            second_player_total += coins[-1]
            coins = coins[:-1]
        
        if coins[0] > coins[-1]:
            first_player_total += coins[0]
            coins = coins[1:]
        else:
            first_player_total += coins[-1]
            coins = coins[:-1]
    
    if first_player_total > second_player_total:
        return "First player wins."
    elif first_player_total < second_player_total:
        return "Second player wins."
    else:
        return "tie."

coins = [18, 20, 15, 30, 10, 14]
print(coin_game_strategy(coins)) 
