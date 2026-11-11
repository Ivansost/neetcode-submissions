class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
                
            elif not stack:
                return False 
                
            else:
                cur = stack.pop()
                if cur == "[" and char != "]":
                    return False
                elif cur == "{" and char != "}":
                    return False
                elif cur == "(" and char != ")":
                    return False 
        return not stack 