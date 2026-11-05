class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        num = 0
        colMap = dict()
        
        for i in nums:
            colMap[i] = colMap.get(i,0) + 1
            
        for i in range(colMap.get(0, 0)):
            nums[num] = 0
            num += 1

        for i in range(colMap.get(1, 0)):
            nums[num] = 1
            num += 1
        
        for i in range(colMap.get(2, 0)):
            nums[num] = 2
            num += 1
