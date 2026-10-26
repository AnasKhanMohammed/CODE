class Solution:
    def minOperations(self, nums: list[int]) -> int:
        import math

        ops = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                nums[i] = self._smallest_prime_factor(nums[i])
                ops += 1

                if nums[i] > nums[i + 1]:
                    return -1

        return ops

    def _smallest_prime_factor(self, x: int) -> int:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return i
        return x