
class Solution:
    def numberOfChild(self, n, k):
        pos = k % (2 * (n - 1))
        if pos < n:
            return pos
        return 2 * (n - 1) - pos
