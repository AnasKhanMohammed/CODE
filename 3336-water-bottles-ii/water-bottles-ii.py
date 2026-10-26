class Solution:
    def maxBottlesDrunk(self, numBottles, numExchange):
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            empty -= numExchange
            total += 1
            empty += 1
            numExchange += 1

        return total