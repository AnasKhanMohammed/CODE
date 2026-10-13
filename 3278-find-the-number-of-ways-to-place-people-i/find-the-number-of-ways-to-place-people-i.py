class Solution:
    def numberOfPairs(self, points):
        n = len(points)
        ans = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 <= x2 and y1 >= y2:
                    if not any(
                        x1 <= x <= x2 and y2 <= y <= y1
                        for k, (x, y) in enumerate(points)
                        if k != i and k != j
                    ):
                        ans += 1

        return ans