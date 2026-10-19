
class Solution:
    def sumOfEncryptedInt(self, nums):
        total = 0
        for n in nums:
            s = str(n)
            largest = max(s)
            total += int(largest * len(s))
        return total
