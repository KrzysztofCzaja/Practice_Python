# https://leetcode.com/problems/valid-parentheses/
#FIRST
class Solution:
    def isValid(self, s):
        stack, match = [], {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in match:
                if not (stack and stack.pop() == match[ch]):
                    return False
            else:
                stack.append(ch)
        return not stack

test = Solution()
print(test.isValid("()[]{}"))