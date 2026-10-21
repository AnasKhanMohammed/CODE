
class Solution:
    def xorGame(self, nums):
        return len(nums) % 2 == 0 or __import__('functools').reduce(lambda a, b: a ^ b, nums) == 0
