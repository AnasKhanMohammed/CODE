
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount):
        rounded = ((purchaseAmount + 5) // 10) * 10
        return 100 - rounded
