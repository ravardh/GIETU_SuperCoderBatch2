def playerwins(coins):
    sum_first_half = sum(coins[:len(coins)//2])
    sum_second_half = sum(coins[len(coins)//2:])
    
    if sum_first_half > sum_second_half:
        return "frist player wins."
    else:
        return "second player wins."
coins = [18,20,15,30,10,14]
print(playerwins(coins))