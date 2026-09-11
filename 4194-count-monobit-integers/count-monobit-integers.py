class Solution:
    def countMonobit(self, n):
        count = 1  

        x = 1
        while x <= n:
            count += 1
            x = (x << 1) | 1

        return count