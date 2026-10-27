class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i,n= 0,len(nums)
        for j in range(1, n):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
        return i+1

        # by while loop:
        '''
        i, j, n= 1, 1, len(nums)
        while(j<n):
            if nums[i-1]!=nums[j]:
                nums[i]= nums[j]
                i+=1
            j+=1
        return i
        '''     