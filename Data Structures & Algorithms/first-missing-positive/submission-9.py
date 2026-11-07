class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prev = 0
        i = 0

        while i < len(nums):
            if nums[i] <= prev:  # skip negatives, zero, and duplicates
                i += 1
                continue

            if nums[i] > prev + 1:
                return prev + 1

            prev = nums[i]
            i += 1

        return prev + 1