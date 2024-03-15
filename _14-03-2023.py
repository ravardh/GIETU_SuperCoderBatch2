#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fractional_knapsack(W, N, PW, PP):
    items = [(PP[i] / PW[i], PW[i], PP[i]) for i in range(N)]
    items.sort(reverse=True)
    
    total_profit = 0
    for item in items:
        if W >= item[1]:  
            W -= item[1]
            total_profit += item[2]
        else:  
            fraction = W / item[1]
            total_profit += fraction * item[2]
            break  
        
    return total_profit
W = 15
N = 4
PW = [5, 10, 10, 5]
PP = [10, 5, 5, 10]

print("Max Profit:", fractional_knapsack(W, N, PW, PP))


# In[3]:


def winning_strategy(coins):
    n = len(coins)
    if sum(coins[::2])>sum(coins[1::2]):
        return "First player wins."
    else:
        return "Second player wins."

coins = [18,20,15,30,10,14]
result = winning_strategy(coins)
print("Result:",result)


# In[4]:


def find_winner(N,K):
    children=list(range(1,N+1))
    current_index=0
    while len(children)>1:
        remove_index=(current_index+K-1)%len(children)
        children.pop(remove_index)
        current_index=remove_index
    return children[0]

N = 14
K = 20
print("The winning child is:",find_winner(N,K))


# In[7]:


def max_treasure_locations(locations, compass_range):
    max_locations = 0
    for i in range(len(locations)):
        current_locations = set()
        for j in range(i, min(len(locations), i + compass_range)):
            current_locations.add(locations[j])
            max_locations = max(max_locations, len(current_locations))
    return max_locations

locations = [2, 7, 1, 4, 8, 3, 5]
compass_range = 4

print("Maximum number of potential treasure locations:", max_treasure_locations(locations, compass_range))


# In[ ]:


def longest_subarray_with_zero_sum(arr):
    prefix_sum=0
    max_length=0
    sum_index={}
    
    for i, num in enumerate(arr):
        prefix_sum+=num
        if num==0 and max_length==0:
            max_length=1
        if prefix_sum==0:
            max_length=i+1
        if prefix_sum in sum_index:
            max_length=max(max_length,i-sum_index[prefix_sum])
        else:
            sum_index[prefix_sum]=i
    return max_length
    
arr=list(map(int, input().split()))
result=longest_subarray_with_zero_sum(arr)
print("Result:",result)


# In[ ]:




