class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False

        for i in range(len(s)):
            if s[i] == ")" :
                if not stack or stack.pop() != "(":
                    return False

            elif s[i] == "]" :
                if not stack or stack.pop() != "[":
                    return False

            elif s[i] == "}" :
                if not stack or stack.pop() != "{":
                    return False
            
            else:
                stack.append(s[i])
        return not stack
