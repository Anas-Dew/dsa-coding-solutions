#  Problem Link -> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Solution
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfits = 0
        step = 1
        for i in range(0, len(prices)-1, step):
            if prices[i+1] > prices[i] :
                maxProfits += prices[i+1] - prices[i]
                step = 2
            else :
                step = 1
        return maxProfits

# Notes -> Initialize two values -> maxProfits and step.
# Iterate through the array from 0 to list length-1. and step is for jumping because we cannot buy sell twice a day.
# if next day price is higher than today's price then -> next day price - today's price = today profit.
# add it to maxProfits, and skip next day and goto another day and so on.
# if next day price is not higher than today's price then -> do thing and move on. ref: else condition. step = 1 will do nothing but step = 2 skips a day.