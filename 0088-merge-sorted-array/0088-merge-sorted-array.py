class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if n<=0:
            return nums1
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()