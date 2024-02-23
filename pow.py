class Solution(object):
    def myPow(self, x: float, n: int) -> float:
        """
        Calculates x raised to the power n (i.e., x^n).

        Args:
            x: The base number.
            n: The exponent.

        Returns:
            The result of x raised to the power n.

        Raises:
            ValueError: If n is negative and x is 0.
        """

        if n == 0:
            return 1.0
        elif n < 0:
            if x == 0:
                raise ValueError("Cannot calculate x^n for x=0 and n<0")
            return 1.0 / self.myPow(x, -n)
        else:
            result = 1.0
            while n > 0:
                if n % 2 == 1:
                    result *= x
                x *= x
                n //= 2
            return result

# Example usage:
solution = Solution()
result = solution.myPow(2.0, 10)  # 1024.0
result = solution.myPow(2.1, 3)   # 9.261
# result = solution.myPow(0.0, -2)  # Would raise ValueError
