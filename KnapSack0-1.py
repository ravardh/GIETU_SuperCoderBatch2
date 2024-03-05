def knapSack(item, price, weight, knapWeight):
    knap = {}
    pw = [0] * len(item)
    

    for i in range(len(item)):
        pw[i] = price[i] / weight[i]
        knap[item[i]] = pw[i]
    
    knap = dict(sorted(knap.items(), key=lambda x: x[1], reverse=True))
    
    req_weight = 0
    selected_items = []

    for key, value in knap.items():
        if req_weight + weight[key] <= knapWeight:
            req_weight += weight[key]
            selected_items.append(key)
    
    return selected_items

price = [60, 100, 120]
weight = [10, 20, 30]
W = 50
items = [0, 1, 2]
print(knapSack(items, price, weight, W))
