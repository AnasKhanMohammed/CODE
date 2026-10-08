class Solution:
    def hasGroupsSizeX(self, deck):
        count = {}

        for card in deck:
            count[card] = count.get(card, 0) + 1

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        x = 0

        for freq in count.values():
            x = gcd(x, freq)

        return x > 1