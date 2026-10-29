class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dic= {}
        n= len(nums)

        for num in nums:
            dic[num]= dic.get(num, 0)+ 1

        # m3
        n= n//2
        for k,v in dic.items():
            if v>n: return k
        return 0


        # m1:
        '''
        m, op= 0,0
        for k,v in dic.items():
            if count>m:
                m, op= count, i
        return op
        '''
        # m2
        ''' op= max(dic, key=dic.get)
        return op '''
