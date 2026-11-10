class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        l = 0
        blankarr = [None] * len(nums)

        while l < len(nums):
            newad = 0
            
            if l + k > len(nums) - 1:
                newad = k - (len(nums) - l)
                
                blankarr[newad] = nums[l]
            else:
                
                blankarr[l+k] = nums[l]

            l += 1

        nums[:] = blankarr