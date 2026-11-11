class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for cur in s:
            if cur == '(' or cur == '[' or cur == '{':
                stack.append(cur)
            
            else:
                if len(stack) == 0:
                    return False

                openingbracket = stack.pop()

            if cur == ')' and openingbracket != '(':
                return False
            elif cur == '}' and openingbracket != '{':
                return False
            elif cur == ']' and openingbracket != '[':
                return False

        if len(stack) == 0:
            return True
        else:
            return False