class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        ans = []
        used = [0] * len(nums)

        def bt(path):
            if len(path) == len(nums):
                ans.append(path[:]); return
            for i in range(len(nums)):
                if used[i] or (i and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                used[i] = 1; path.append(nums[i])
                bt(path)
                path.pop(); used[i] = 0

        bt([])
        return ans