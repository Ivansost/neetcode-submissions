class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        savePrefix = ""
        for length in range(1, len(strs[0]) + 1):
            prefix = strs[0][:length]

            for word in strs:
                if word[:length] != prefix:
                    return word[:length - 1]

           

            savePrefix = prefix
        
        return savePrefix