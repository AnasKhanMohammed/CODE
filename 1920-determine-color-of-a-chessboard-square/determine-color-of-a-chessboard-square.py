
class Solution:
    def squareIsWhite(self, coordinates):
        return (ord(coordinates[0]) - ord('a') + int(coordinates[1])) % 2 == 0
