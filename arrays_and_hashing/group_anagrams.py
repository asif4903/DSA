# Leetcode link: https://leetcode.com/problems/group-anagrams/
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
            
        return list(anagram_map.values())


strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]

print(Solution().groupAnagrams(strs))
