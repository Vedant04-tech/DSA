class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dic= {}
        n= len(nums)

        for num in nums:
            dic[num]= dic.get(num, 0)+ 1

        m, op= 0,0
        for i, count in dic.items():
            if count>m:
                m, op= count, i
        # op= max(dic, key=dic.get) 
        return op