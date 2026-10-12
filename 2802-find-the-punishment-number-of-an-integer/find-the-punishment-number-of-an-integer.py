
class Solution:
    def punishmentNumber(self, n):
        def check(s, target):
            if not s:
                return target == 0
            for i in range(1, len(s) + 1):
                if check(s[i:], target - int(s[:i])):
                    return True
            return False

        total = 0
        for i in range(1, n + 1):
            sq = i * i
            if check(str(sq), i):
                total += sq
        return total
