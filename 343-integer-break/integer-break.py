class Solution:
    def integerBreak(self, n):
        if n <= 3:
            return n - 1

        result = 1

        while n > 4:
            result *= 3
            n -= 3

        return result * n