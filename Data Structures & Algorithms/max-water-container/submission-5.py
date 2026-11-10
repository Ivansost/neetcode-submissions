class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        maxw = 0

        while l < r:

            length = r - l

            h = min(heights[l],heights[r])

            a = h * length

            if a > maxw:
                maxw = a
            
            if heights[l] >heights[r]:
                r -= 1

            else:

                l+=1
                
        return maxw