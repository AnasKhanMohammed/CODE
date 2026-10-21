
class Solution:
    def selfDividingNumbers(self, left, right):
        res = []

        for num in range(left, right + 1):
            if '0' not in str(num) and all(num % int(d) == 0 for d in str(num)):
                res.append(num)

        return res
