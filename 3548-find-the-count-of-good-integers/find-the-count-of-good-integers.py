from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        fact = [factorial(i) for i in range(n + 1)]
        seen = set()
        ans = 0

        half = (n + 1) // 2

        for i in range(10 ** (half - 1), 10 ** half):
            s = str(i)
            pal = s + (s[:-1][::-1] if n % 2 else s[::-1])

            if int(pal) % k != 0:
                continue

            freq = [0] * 10
            for ch in pal:
                freq[int(ch)] += 1

            key = tuple(freq)
            if key in seen:
                continue
            seen.add(key)

            count = fact[n - 1] * (n - freq[0])

            for f in freq:
                count //= fact[f] if False else 1

            denom = 1
            for f in freq:
                denom *= fact[f]

            ans += count // denom

        return ans