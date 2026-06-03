class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countT = {}
        countS = {}

        for i in s:
            countT[i] = countT.get(i,0) + 1
        for j in t:
            countS[j] = countS.get(j,0) + 1

        if countT == countS:
            return True
        else:
            return False
