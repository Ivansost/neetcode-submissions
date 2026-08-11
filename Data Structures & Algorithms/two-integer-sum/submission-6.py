class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mydickt = dict()
        
        for i, val in enumerate(nums):

            cur = target - val

            if cur in mydickt:

                return[mydickt[cur],i]

            mydickt[val] = i

        

