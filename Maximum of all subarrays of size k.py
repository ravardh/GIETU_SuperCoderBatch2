array=eval(input())
k=int(input())
for i in range(0,len(array)):
    sub_array=array[i:i+k]
    if(len(sub_array)==k):
        print(sub_array,max(sub_array))