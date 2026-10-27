class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, k, n= 0, 0, len(nums)
        while i<n:
            if nums[i]!= val:
                nums[k]= nums[i]
                k+=1
            i+=1
        return k

        # or other method:
        '''
        k, n= 0, len(nums)
        for i in range(n):
            if nums[i]!= val:
                nums[k]= nums[i]
                k+=1
        return k
        '''