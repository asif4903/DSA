# leetcode link: https://leetcode.com/problems/valid-palindrome/

class Solution:
    # in O(n) time complexity with O(n) space complexity as well
    # def isPalindrome(self, s: str) -> bool:
    #     filtered_str = ""
    #     for c in s:
    #         lc = c.lower()
    #         if (
    #             ord("A") <= ord(c) <= ord("Z")
    #             or ord("a") <= ord(c) <= ord("z")
    #             or ord("0") <= ord(c) <= ord("9")
    #             ):
    #             filtered_str += lc
    #     print(filtered_str)
    #     if len(filtered_str) == 0 or len(filtered_str) == 1:
    #         return True

    #     for i in range((len(filtered_str) // 2) + 1):
    #         if filtered_str[i] != filtered_str[len(filtered_str) - 1 - i]:
    #             return False
    #     return True

    # Time complexity is O(n) and space complexity is O(1)
    def isPalindrome(self, s: str) -> bool:
        # we are going to use two pointers
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function

    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


s = "0P"
# amanaplanacanalpanama
print(Solution().isPalindrome(s))
