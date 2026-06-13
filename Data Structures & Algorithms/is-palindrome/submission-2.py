class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        
        #checking if the left is less then right (waiting for mdidle)
        while left < right:
            #making sure its not middle and making sure if its not a real number or letter we incramenrt
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
#if they are the same incrament
            if s[left] == s[right]:
                left += 1
                right -= 1
                #if not we return false
            else:
                return False
                #true
        return True