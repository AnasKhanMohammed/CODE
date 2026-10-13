class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        a = [x for row in grid for x in row]
        for i in range(1, n*n + 1):
            if a.count(i) == 2:
                r = i
            if a.count(i) == 0:
                m = i
        return [r, m]