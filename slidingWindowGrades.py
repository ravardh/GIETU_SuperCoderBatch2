grades=[1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]

n=int(input("Enter value of n:"))
# def findSum(grades,i,n):
#     sum=0
#     for i in range(i,n+1):
#         sum+=grades[i]
#     return sum
# maxSum=0
# a=-1
# c=-1
# b=-1
# for i in range(0,len(grades)):
#     if(i+n<len(grades)):
#         sum=findSum(grades,i,i+n-1)
#         if(sum>=maxSum)
#             maxSum=sum
            
# print(maxSum)
sum=0
maxSum=0
i=0
while(i<len(grades)):
    sum+=grades[i]
    if(i>=n-1):
        maxSum=max(sum,maxSum)
        sum=sum-grades[i-n+1]
    i=i+1
print(maxSum)