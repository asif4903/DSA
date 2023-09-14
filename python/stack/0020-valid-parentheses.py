# leedcode link: https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
      stack = []
      d = {"(": ")", "{": "}", "[": "]"}
      for c in s:
        if c in d:  # 1
          stack.append(c)
        elif len(stack) == 0 or d[stack.pop()] != c:  # 2
          return False

      return len(stack) == 0  # 3

# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket


s = "()[]{}"
print(Solution().isValid(s))
