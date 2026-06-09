class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #initalize a set
        setnums = set()
        longest = 0
        #loop though the array add add each indicies to the set
        for i in range(len(nums)):
            setnums.add(nums[i])

        #loop thorugh the set
        for j in setnums:
            #checking j - 1 which checks if there is something that exists before j in the set(first value)
            if j - 1 not in setnums:
                #now we set the length to 1
                length = 1
                #checking if the number is 1 up in nums
                while j + length in setnums:
                    #increase the next count 
                    length += 1
                #if the lengeth is greater to the longest we set it to the longest so new long is the longest
                if length > longest:
                    longest = length
        #return the logest sequance
        return longest
