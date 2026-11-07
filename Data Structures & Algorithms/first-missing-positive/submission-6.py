class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        expected = 1

        for num in sorted(nums):
            if num == expected:
                expected += 1

        return expected