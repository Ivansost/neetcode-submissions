class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        once = set()

        for i in range(len(nums)):
            
            once.add(nums[i])
                
        nums[:] = sorted(once)
        return len(nums)