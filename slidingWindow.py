a=[1,3,5,3,7,4,8,9,5,3,5,7,9,3,2,0]

k= int(input("Enter number of terms:"))
sum_arr=[]

for i in range(len(a)-(k-1)):
    sum1 = sum(a[i:i+k])
    sum_arr.append(sum1)

max_sum = max(sum_arr)
max_index = sum_arr.index(max_sum)
print(max_sum)
print(a[max_index:max_index+k])