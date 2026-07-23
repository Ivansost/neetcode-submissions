class Solution:
    def isValid(self, s: str) -> bool:
        leftStack = []

        for current in s:

            #if the perenthisis is open then we add it to the stack
            if current == "(" or current == "[" or current == "{":
                leftStack.append(current)

            else:
                #closing parenthesis has nothing to match
                if not leftStack:
                    return False

                opening = leftStack.pop()

                #check each possible closing parenthesis
                if current == ")" and opening != "(":
                    return False

                elif current == "]" and opening != "[":
                    return False

                elif current == "}" and opening != "{":
                    return False

        if len(leftStack) == 0:
            return True
        else:
            return False