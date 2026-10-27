class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i, j, n= 0, 1, len(nums)

        while(j<n):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]= nums[j]
            j+=1
        return i+1
                