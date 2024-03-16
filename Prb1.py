def prb(W, N, PW, PP):
      
    items = [(PP[i]/PW[i], PW[i], i) for i in range(N)]
    
     
    items.sort(reverse=True)
    
    max_profit = 0
    
    for item in items:
        if W == 0:
            break
        if item[1] <= W:   
            max_profit += item[0] * item[1]   
            W -= item[1]   
        else:   
            max_profit += item[0] * W   
            W = 0  
    
    return max_profit

 
W = 15
N = 4   
PW = [5, 10, 10, 5]
PP = [10, 5, 5, 10]

print("Max Profit:", prb(W, N, PW, PP))
