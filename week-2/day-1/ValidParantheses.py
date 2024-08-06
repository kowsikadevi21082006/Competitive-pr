class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
    
        for char in s:
            if char in dict.keys():
                stack.append(char)
            elif char in dict.values():
                if not stack or dict[stack.pop()] != char:
                    return False
        return not stack
        