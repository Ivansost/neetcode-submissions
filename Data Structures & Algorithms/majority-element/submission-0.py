class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        countdict = dict()

        for i in nums:
            countdict[i] = countdict.get(i,0) + 1

        most_common = max(countdict, key=countdict.get)

        return most_common
