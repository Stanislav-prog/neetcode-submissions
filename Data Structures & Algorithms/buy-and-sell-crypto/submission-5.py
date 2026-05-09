class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if (prices[i] < prices[j]) and (prices[j] - prices[i] > res):
                    res = prices[j] - prices[i]
        return res
