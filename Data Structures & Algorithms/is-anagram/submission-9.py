class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictonary1 = {}
        dictonary2 = {}

        if len(s) != len(t):
            return False

        for i in s:
            dictonary1[i] = dictonary1.get(i,0) + 1

        for j in t:
            dictonary2[j] = dictonary2.get(j,0) + 1

        if dictonary2 == dictonary1:
            return True
        else:
            return False