def Fact(n):
    if n==0:
        return 1
    else:
        return n* Fact(n-1)
    
try:
    num=int(input("Enter the number to be factored:"))  
    if (num<0):
        print("Please enter a +ve number.")  
    else:
        print("Factorial of ",num, "is",Fact(num))

except ValueError:
    print("Please enter  a valid number.")            
