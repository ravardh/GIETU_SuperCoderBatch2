array=eval(input())
size=int(input())
for i in range(0,len(array)):
    sub_array=array[i:i+size]
    if(len(sub_array)==size):
        print(sub_array,max(sub_array))
