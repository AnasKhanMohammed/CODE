
class Solution:
    def largestMultipleOfThree(self, digits):
        digits.sort(reverse=True)
        r = sum(digits) % 3

        for rem, count in [(r, 1), (3-r, 2)]:
            if r == 0:
                break
            temp = sorted(d for d in digits if d % 3 == rem)
            if len(temp) >= count:
                for d in temp[:count]:
                    digits.remove(d)
                break
        else:
            return ""

        if not digits:
            return ""
        if digits[0] == 0:
            return "0"
        return ''.join(map(str, digits))
