"""5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.longestPalindrome(*args, **kwargs)

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        left = 0
        pali_start = 0
        pali_len = 1
        for i in range(n):
            right = i
            while right < n and s[right] == s[i]:
                right += 1

            left = i - 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            left = left + 1
            if pali_len < right - left:
                pali_len = right - left
                pali_start = left

        return s[pali_start: pali_start + pali_len]
