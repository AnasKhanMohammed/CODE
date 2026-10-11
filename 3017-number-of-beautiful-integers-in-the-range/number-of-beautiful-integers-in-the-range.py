
class Solution:
    def numberOfBeautifulIntegers(self, low, high, k):
        def f(n):
            s = str(n)
            memo = {}

            def dp(i, b, r, started, tight):
                if i == len(s):
                    return int(started and b == 0 and r == 0)
                key = (i, b, r, started, tight)
                if key in memo:
                    return memo[key]
                ans = 0
                for d in range((int(s[i]) if tight else 9) + 1):
                    ans += dp(i+1, b if not started and d == 0 else b+(1 if d%2 else -1),
                              (r*10+d)%k if started or d else r,
                              started or d > 0, tight and d == int(s[i]))
                memo[key] = ans
                return ans

            return dp(0, 0, 0, False, True)

        return f(high) - f(low-1)
