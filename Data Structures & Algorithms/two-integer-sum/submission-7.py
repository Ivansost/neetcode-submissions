class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictmap = dict()

        for key, val in enumerate(nums):
            
            find = target - val

            if find in dictmap:
                return [dictmap[find],key]
            
            dictmap[val] = key