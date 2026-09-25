class Solution:
    def countDigitOne(self, n):
        count = 0
        factor = 1

        while factor <= n:
            low = n % factor
            cur = (n // factor) % 10
            high = n // (factor * 10)

            if cur == 0:
                count += high * factor
            elif cur == 1:
                count += high * factor + low + 1
            else:
                count += (high + 1) * factor

            factor *= 10

        return count