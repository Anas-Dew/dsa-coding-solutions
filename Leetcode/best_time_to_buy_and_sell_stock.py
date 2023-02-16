class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # l, r = 0, 1
        # maxProfit = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         currentProfit = prices[r] - prices[l]
        #         maxProfit = max(currentProfit, maxProfit)
        #     else:
        #         l = r
        #     r +=1
        # return maxProfit
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

if __name__ == "__main__" :
    test = Solution()
    print(test.maxProfit([7,1,5,3,6,4]))