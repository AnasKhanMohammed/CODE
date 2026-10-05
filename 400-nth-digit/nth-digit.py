class Solution:
    def findNthDigit(self, n):
        d = 1
        count = 9

        while n > d * count:
            n -= d * count
            d += 1
            count *= 10

        num = 10 ** (d - 1) + (n - 1) // d
        return int(str(num)[(n - 1) % d])