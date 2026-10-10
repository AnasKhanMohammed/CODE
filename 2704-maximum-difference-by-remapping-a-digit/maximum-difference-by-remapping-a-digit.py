
class Solution:
    def minMaxDifference(self, num):
        s = str(num)

        max_num = s.replace(next((c for c in s if c != '9'), '9'), '9')
        min_num = s.replace(s[0], '0')

        return int(max_num) - int(min_num)
