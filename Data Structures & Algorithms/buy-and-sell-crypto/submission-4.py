class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_ptr, r_ptr = 0, 1
        maxP = 0

        while r_ptr < len(prices):

            if prices[l_ptr] < prices[r_ptr]:
                profit = prices[r_ptr] - prices[l_ptr]
                maxP = max(maxP, profit)
            else:
                l_ptr = r_ptr
            
            r_ptr += 1
        
        return maxP
        