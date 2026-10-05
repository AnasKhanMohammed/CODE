class Solution:
    def isHappy(self, n):
        s = set()
        while n != 1:
            if n in s: return False
            s.add(n)
            n = sum(int(x)**2 for x in str(n))
        return True