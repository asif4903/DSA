# leetcode link: https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in num_set:
            # check if it's a start of a sequence
            if (n - 1) not in num_set:
                sequence_length = 1
                while (n + sequence_length) in num_set:
                    sequence_length += 1
                longest = max(longest, sequence_length)
        return longest


nums = [100,4,200,1,3,2]

print(Solution().longestConsecutive(nums))