
# leetcode link: https://leetcode.com/problems/trapping-rain-water


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        max_left = height[0]
        max_right = height[-1]
        point_left = 1
        point_right = len(height) - 2
        trapping_rain_water_amount = 0

        while point_left <= point_right:
            if max_left < height[point_left]:
                max_left = height[point_left]
            if max_right < height[point_right]:
                max_right = height[point_right]

            if max_left < max_right:
                trapping_rain_water_amount += max_left - height[point_left]
                point_left += 1
            else:
                trapping_rain_water_amount += max_right - height[point_right]
                point_right -= 1
        return trapping_rain_water_amount


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(Solution().trap(height))
