#Without recursion
'''
class Solution:
    def myPow(self, x: float, n: int):
        if n==0:
            return 1
        elif n<0:
            return 1
        else:
            return x * self.myPow(x, n - 1)

sol = Solution()
x =int(input("Enter a number: ")) #2.0
n =int(input("Enter the power of that number: ")) #6
print(sol.myPow(x,n))
'''
#With recursion
def Pow(a,b):
    if(b==0):
        return 1
    else:
        return a*Pow(a,b-1)
a=int(input("enter a number: "))
b=int(input("enter the power of the number: "))
print("Power is: ",Pow(a,b))
