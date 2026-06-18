class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        letterSet = set()
        longest = 0
        #loop through the string
        for right in range(len(s)):
            #if the number alerady exists in the set, remove it and incrament left + 1
            while s[right] in letterSet:
                letterSet.remove(s[left])
                left += 1
            #add the new one to it (current index)
            letterSet.add(s[right])
            
            length = right - left + 1
            #if the length == lognest then update
            if length > longest:
                longest = length
        #return the longest
        return longest