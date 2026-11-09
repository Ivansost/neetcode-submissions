class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        left = m
        l2 = 0

        while l2 < n:
            nums1[left] = nums2[l2]
            left += 1
            l2 += 1

        nums1.sort()