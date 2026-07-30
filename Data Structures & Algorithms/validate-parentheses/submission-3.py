class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['[', '{', '(']
        stack = []
        
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                
                left_bracket = stack.pop()
                if left_bracket == '[' and bracket == ']' or \
                    left_bracket == '{' and bracket == '}' or \
                    left_bracket == '(' and bracket == ')':
                    continue
                else:
                    return False

        return len(stack) == 0