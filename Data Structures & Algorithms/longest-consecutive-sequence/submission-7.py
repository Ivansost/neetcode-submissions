class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        numsSet = set(nums)

        longest = 0

        for j in numsSet:
            if (j - 1) not in numsSet:
                length = 1

                while j + length in numsSet:

                    length += 1
            
                if length > longest:
                    longest = length
                
        return longest

