class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        unique = set()
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        quad = (nums[i], nums[j], nums[l], nums[r])

                        unique.add(quad)

                        r -= 1
                        l += 1


                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1

        return list(unique)