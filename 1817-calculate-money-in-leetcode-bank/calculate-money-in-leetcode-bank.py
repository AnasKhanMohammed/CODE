
class Solution:
    def totalMoney(self, n):
        total = 0
        week = 0

        while n > 0:
            for day in range(1, min(n, 7) + 1):
                total += week + day
            n -= 7
            week += 1

        return total
