class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0

        right = len(heights) - 1

        total = 0

        while left < right:

            length = right - left

            height = min(heights[left], heights[right])

            area  = height * length

            if area > total:

                total = area

            if heights[left] < heights[right]:

                left += 1
            
            else:

                right -= 1
        
        return total