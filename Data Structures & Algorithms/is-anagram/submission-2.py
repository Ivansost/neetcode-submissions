class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dickS = {}
        dickT = {}

        for i in s:
            dickS[i] = dickS.get(i,0) + 1
        for j in t:
            dickT[j] = dickT.get(j,0) + 1

        if dickS == dickT:
            return True
        else:
            return False
        
        