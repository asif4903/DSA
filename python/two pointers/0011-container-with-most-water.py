# leetcode link: https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = float("-inf")
        l, r = 0, len(height) - 1
        while l < r:
            length = r - l
            h = min(height[l], height[r])
            area = length * h
            ans = max(area, ans)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))
