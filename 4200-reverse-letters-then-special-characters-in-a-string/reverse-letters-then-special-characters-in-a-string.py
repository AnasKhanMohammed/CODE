class Solution:
    def reverseByType(self, s):
        letters = [c for c in s if c.islower()]
        specials = [c for c in s if not c.islower()]

        letters.reverse()
        specials.reverse()

        i = j = 0
        ans = []

        for c in s:
            if c.islower():
                ans.append(letters[i])
                i += 1
            else:
                ans.append(specials[j])
                j += 1

        return "".join(ans)