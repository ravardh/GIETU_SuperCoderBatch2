class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x, n - 1)
solution = Solution()
x1, n1 = 2.00000, 10
x2, n2 = 2.10000, 3
x3, n3 = 2.00000, -2

print(solution.myPow(x1, n1))  
print(solution.myPow(x2, n2))
print(solution.myPow(x3, n3)) 