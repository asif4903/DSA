# leetcode link: https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        counter = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in counter.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans

nums = [1,1,1,2,2,3]
k = 2

print(Solution().topKFrequent(nums, k))