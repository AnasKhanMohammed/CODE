class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        required = [0] * 4

        for i, p in enumerate([2, 3, 5, 7]):
            while t % p == 0:
                required[i] += 1
                t //= p

        if t != 1:
            return "-1"

        digit_factors = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [3, 0, 0, 0],
            [0, 2, 0, 0]
        ]

        def make_digits(count):
            a, b, c, d = count

            count8, a = divmod(a, 3)
            count9, b = divmod(b, 2)
            count4, count2 = divmod(a, 2)
            count3 = b
            count6 = 0

            if count2 == 1 and count3 == 1:
                count2 = count3 = 0
                count6 = 1

            if count3 == 1 and count4 == 1:
                count2 = 1
                count6 = 1
                count3 = count4 = 0

            return (
                '2' * count2 +
                '3' * count3 +
                '4' * count4 +
                '5' * c +
                '6' * count6 +
                '7' * d +
                '8' * count8 +
                '9' * count9
            )

        def subtract(a, b):
            return [max(0, a[i] - b[i]) for i in range(4)]

        def digit_count(s):
            count = [0] * 4

            for ch in s:
                f = digit_factors[ord(ch) - ord('0')]
                for j in range(4):
                    count[j] += f[j]

            return count

        def fits(count, length):
            return len(make_digits(count)) <= length

        n = len(num)
        first_zero = num.find('0')

        if first_zero == -1:
            first_zero = n
            current = digit_count(num)

            if all(current[i] >= required[i] for i in range(4)):
                return num

        if len(make_digits(required)) > n:
            return make_digits(required)

        prefix_count = digit_count(num)

        for i in range(n - 1, -1, -1):
            f = digit_factors[ord(num[i]) - ord('0')]

            for j in range(4):
                prefix_count[j] -= f[j]

            if i > first_zero:
                continue

            for d in range(int(num[i]) + 1, 10):
                need = subtract(required, prefix_count)

                for j in range(4):
                    need[j] = max(0, need[j] - digit_factors[d][j])

                suffix_len = n - i - 1

                suffix = make_digits(need)

                if len(suffix) <= suffix_len:
                    ones = '1' * (suffix_len - len(suffix))
                    return num[:i] + str(d) + ones + suffix

        result = make_digits(required)
        return '1' * (n + 1 - len(result)) + result