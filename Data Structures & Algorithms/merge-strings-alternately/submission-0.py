class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        if len(word1) < len(word2):
            shortestWord = word1
        else:
            shortestWord = word2

        length = len(shortestWord) - 1
        left = 0

        arr = []
        
        while left <= length:
            arr.append(word1[left])
            arr.append(word2[left])
            left+=1

        
        arr.append(word1[left:])
        arr.append(word2[left:])
        
        return "".join(arr)