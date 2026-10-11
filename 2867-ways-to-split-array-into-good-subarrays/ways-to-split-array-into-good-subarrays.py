
class Solution:
    def numberOfGoodSubarraySplits(self, nums):
        MOD = 10**9 + 7
        ans = 1
        prev = -1

        for i, x in enumerate(nums):
            if x == 1:
                if prev != -1:
                    ans = ans * (i - prev) % MOD
                prev = i

        return ans if prev != -1 else 0
