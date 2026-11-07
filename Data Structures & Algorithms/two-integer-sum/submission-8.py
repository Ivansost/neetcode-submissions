class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictmap = dict()

        for key, val in enumerate(nums):

            value = target - nums[key]

            if value in dictmap:
                return [dictmap[value], key] 

            dictmap[val] = key