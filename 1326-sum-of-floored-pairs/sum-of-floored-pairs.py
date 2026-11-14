class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)

        freq = [0] * (max_num + 1)

        for num in nums:
            freq[num] += 1

        prefix = [0] * (max_num + 1)

        for i in range(1, max_num + 1):
            prefix[i] = prefix[i - 1] + freq[i]

        ans = 0

        for x in range(1, max_num + 1):
            if freq[x] == 0:
                continue

            total = 0

            for start in range(x, max_num + 1, x):
                end = min(start + x - 1, max_num)

                count = prefix[end] - prefix[start - 1]

                total += (start // x) * count

            ans = (ans + freq[x] * total) % MOD

        return ans