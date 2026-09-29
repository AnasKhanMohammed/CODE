class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1] * n
        index = [0] * len(primes)

        for i in range(1, n):
            next_num = min(
                ugly[index[j]] * primes[j]
                for j in range(len(primes))
            )

            ugly[i] = next_num

            for j in range(len(primes)):
                if ugly[index[j]] * primes[j] == next_num:
                    index[j] += 1

        return ugly[n - 1]