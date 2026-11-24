
class Solution:
    def rotatedDigits(self, n):
        count = 0

        for i in range(1, n + 1):
            num = str(i)

            if any(d in "2569" for d in num) and all(d in "0125689" for d in num):
                count += 1

        return count
