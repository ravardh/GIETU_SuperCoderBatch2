class Solution:
    def myPow(self, x: float, n: int):
        if n==0:
            return 1
        elif n<0:
            return 1
        
        else:
            return x * self.myPow(x, n - 1)
sol = Solution()
x = 2.0
n = 6
print(sol.myPow(x, n))