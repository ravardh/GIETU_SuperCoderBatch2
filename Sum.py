def sum(a,b):
    sum=0
    if(a>0 and b>0):
          sum=a+b
          return sum
    else:
         print("Enter a validv num.") 
a=int(input("Enter a num:"))   
b=int(input("Enter a num:"))  
sum(a,b)
print (sum) 