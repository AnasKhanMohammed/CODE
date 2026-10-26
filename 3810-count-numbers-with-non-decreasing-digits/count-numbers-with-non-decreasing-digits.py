class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 10**9 + 7

        def convert(s):
            digits = []
            while s != "0":
                rem = 0
                quotient = []

                for ch in s:
                    cur = rem * 10 + int(ch)
                    q, rem = divmod(cur, b)

                    if quotient or q:
                        quotient.append(str(q))

                digits.append(rem)
                s = ''.join(quotient) if quotient else "0"

            return digits[::-1]

        def decrement(s):
            arr = list(s)
            i = len(arr) - 1

            while arr[i] == '0':
                arr[i] = '9'
                i -= 1

            arr[i] = str(int(arr[i]) - 1)
            result = ''.join(arr).lstrip('0')
            return result if result else "0"

        def count_up_to(s):
            digits = convert(s)
            n = len(digits)

            dp = {(0, 0, 1): 1}

            for pos in range(n):
                ndp = {}

                for (last, started, tight), ways in dp.items():
                    limit = digits[pos] if tight else b - 1

                    for d in range(limit + 1):
                        ntight = int(tight and d == limit)

                        if not started and d == 0:
                            key = (0, 0, ntight)
                        else:
                            if started and d < last:
                                continue
                            key = (d, 1, ntight)

                        ndp[key] = (ndp.get(key, 0) + ways) % MOD

                dp = ndp

            return sum(
                ways for (last, started, tight), ways in dp.items()
            ) % MOD

        lower = decrement(l)

        return (count_up_to(r) - count_up_to(lower)) % MOD