class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_pr, max_p= float('inf'), 0

        for p in prices:
            if p<min_pr: min_pr= p
            profit= p- min_pr
            if profit> max_p: max_p= profit
        return max_p