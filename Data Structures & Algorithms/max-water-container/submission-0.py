class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #intitalize left, right, total
        left = 0
        right = len(heights) - 1
        total = 0
        #check if not center(for 2 pointer)
        while left < right:
            #calculate the width and height
            width = right - left
            height = min(heights[left], heights[right])
            #find area
            area = width * height
            #if area is greater then the total then we choose the greater
            if area > total:
                total = area
            #increment the lower one
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        #return total
        return total