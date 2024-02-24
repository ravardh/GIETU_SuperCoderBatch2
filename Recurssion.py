# def fun(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return n*fun(n-1)
# n=int(input("enter t6he num which you wan to factorize "))
# print(fun(n))


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x < 0:
            print("Enter a positive base number.")
            return None
        elif n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            return x * self.myPow(x, n - 1)
n = int(input("Enter the power of the number: "))
x = float(input("Enter the number whose power you want to calculate: "))
solution = Solution()
result = solution.myPow(x, n)
print("Result:", result)
