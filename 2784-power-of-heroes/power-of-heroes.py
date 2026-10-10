
class Solution:
    def sumOfPower(self, nums):
        MOD = 10**9 + 7
        nums.sort()
        total = 0
        s = 0

        for x in nums:
            total = (total + x * x * (x + s)) % MOD
            s = (2 * s + x) % MOD

        return total
