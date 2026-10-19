
class Solution:
    def subarrayLCM(self, nums, k):
        count = 0
        for i in range(len(nums)):
            lcm = 1
            for j in range(i, len(nums)):
                a, b = lcm, nums[j]
                while b:
                    a, b = b, a % b
                lcm = lcm * nums[j] // a

                if lcm == k:
                    count += 1
                elif lcm > k:
                    break
        return count
