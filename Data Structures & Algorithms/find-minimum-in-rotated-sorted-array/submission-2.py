class Solution:
    def findMin(self, nums: List[int]) -> int:
        #basic binary search variables
        left = 0
        right  = len(nums) - 1
        #checking looping while left is less then right
        while left < right:
            #binary search find mid point
            middle = (left+right) // 2
            #if the mid is greater then the right 
            if nums[middle] > nums[right]:
                #we set our new left to 1 infront of the mid
                left = middle + 1
            #if not we set our right to the middle
            else:
                right = middle
        #returning the left value
        return nums[left]

            

    
