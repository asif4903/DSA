# leetcode link: https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 1
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res


s = "pwwkew"

print(Solution().lengthOfLongestSubstring(s))
