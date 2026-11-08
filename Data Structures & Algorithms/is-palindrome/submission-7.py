class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = list(s)


        left = 0
        right = len(s) - 1

        while left <= right:

            if not s[left].isalnum():
                left+=1

            elif not s[right].isalnum():
                right-=1
            else:
            
                if s[left] != s[right]:
                    return False
                else:
                    right -= 1
                    left += 1
            
        return True