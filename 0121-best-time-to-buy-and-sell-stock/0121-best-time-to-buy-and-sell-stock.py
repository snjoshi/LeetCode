class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointer soln
        l,r=0,1
        maxP=0
        profit=0
        while r<len(prices):
            profit=prices[r]-prices[l]
            maxP=max(maxP,profit)
            if prices[r]<prices[l]:
                l=r
            r+=1
        return maxP