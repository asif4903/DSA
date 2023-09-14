# leetcode link: https://leetcode.com/problems/evaluate-reverse-polish-notation

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
          if s == "+":
            stack.append(stack.pop() + stack.pop())
          elif s == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
          elif s == "*":
            stack.append(stack.pop() * stack.pop())
          elif s == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b/a))
          else:
            stack.append(int(s))
        return stack[-1]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(Solution().evalRPN(tokens))
