# Leetcode link: https://leetcode.com/problems/group-anagrams/
from typing import List
from collections import defaultdict
class Solution:
    # using sorted method time complexity O(m*nlog(n))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
            
        return list(anagram_map.values())
    # using count method as chars in string can only be lowercase time complexity: O(m*n)
    def groupAnagramsMoreEfficient(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord("a")] += 1
            anagram_map[tuple(count)].append(word)
        return anagram_map.values()
strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]

print(Solution().groupAnagrams(strs))
print("with efficient solution")
print(Solution().groupAnagramsMoreEfficient(strs))
