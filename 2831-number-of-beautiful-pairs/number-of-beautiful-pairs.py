
class Solution:
    def countBeautifulPairs(self, nums):
        count = 0

        for i in range(len(nums)):
            first = int(str(nums[i])[0])

            for j in range(i + 1, len(nums)):
                last = nums[j] % 10
                a, b = first, last

                while b:
                    a, b = b, a % b

                if a == 1:
                    count += 1

        return count
