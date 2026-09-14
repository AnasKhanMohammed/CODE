class Solution(object):
    def countMonobit(self, n):
        count = 1  # 0

        x = 1
        while x <= n:
            count += 1
            x = (x << 1) | 1

        return count