arr=[]
N=int(input("Enter the size of array:"))
for i in range(N):
    num=int(input("Take elements:"))
    arr.append(num)
maxi=0 
K=int(input("Contiguous subarray:"))
for i in range(len(arr)-K+1):
    for j in range(K):
      if(maxi < arr[i+j]):
         maxi=arr[i+j]
    print(maxi) 
    maxi=0 
       
               

