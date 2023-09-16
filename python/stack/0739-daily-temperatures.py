# leetcode link: https://leetcode.com/problems/daily-temperatures

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_len = len(temperatures)
        res = [0] * temp_len
        stack = []

        for i in range(temp_len - 1, -1, -1):
            while (len(stack) != 0 and temperatures[i] >= temperatures[stack[-1]]):
                stack.pop()
            if len(stack):
                res[i] = stack[-1] - i
            stack.append(i)

        return res


temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]

print(Solution().dailyTemperatures(temperatures))

# Note: We are using monotonically decreasing stack in this problem because stack helps us to look into historcal data while iterating on array.
