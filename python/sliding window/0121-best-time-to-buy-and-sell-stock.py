# leetcode link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            curr_profit = 0
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                profit = max(profit, curr_profit)
            else:
                l = r
            r += 1
        return profit


prices = [7, 1, 5, 3, 6, 4]

print(Solution().maxProfit(prices))
