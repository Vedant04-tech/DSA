class Solution:
    def maxProfit(self, nums: list[int]) -> int:
        n, op= len(nums), 0
        for i in range(1, n):
            if nums[i-1]< nums[i]: op+= nums[i]-nums[i-1]
        return op