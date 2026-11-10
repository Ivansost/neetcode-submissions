class Solution:
    def trap(self, height: List[int]) -> int:

        if height == None:
            return 0

        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        amount = 0

        while l < r:

            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                amount += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                amount += rightMax - height[r]

        return amount