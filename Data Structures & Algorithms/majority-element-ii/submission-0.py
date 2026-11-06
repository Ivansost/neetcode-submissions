class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        amountoftimes = len(nums) / 3

        timesdict = dict()

        result = []

        for i in nums:
            timesdict[i] = timesdict.get(i,0) + 1

        for key in timesdict:
            if timesdict[key] > amountoftimes:
                result.append(key)

        return result