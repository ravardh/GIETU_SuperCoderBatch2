arr = [1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
k = 3
ans = 0
l = 0
check = []

# for i in range(0,len(arr)-k,k):
#     s = arr[i]+arr[i+1]+arr[i+2]
#     if s > ans:
#         ans = s
#         check = [arr[i],arr[i+1],arr[i+2]]

# print(ans)
# print(check)

temp = 0
r = 0
while r < len(arr):
    temp += arr[r]
    if(r-l+1 == k):
        if(temp > ans):
            ans = temp
            check = arr[l:r+1]
        temp-=arr[l]
        l+=1
    r+=1

print(ans)
print(check)