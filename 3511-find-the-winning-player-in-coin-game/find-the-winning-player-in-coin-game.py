class Solution:
    def winningPlayer(self, x, y):
        return "Alice" if min(x, y // 4) % 2 else "Bob"