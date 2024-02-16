class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxt = 0
        minL,minR = 0, 1
        while minR<len(prices):
            if prices[minL] < prices[minR]:
                maxt = max(prices[minR]-prices[minL], maxt)
            else:
                minL = minR
            minR+=1
        return maxt