class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        numSet = set()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    numtriplet = (nums[i], nums[left], nums[right])
                    numSet.add(numtriplet)

                    right -= 1
                    left += 1

                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else: 
                    left += 1
        
        return list(numSet)