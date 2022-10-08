"""5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.longestPalindrome(*args, **kwargs)

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        table = [[False] * n for _ in range(n)]
        for i in range(n):
            table[i][i] = True

        pali_start: int = 0
        max_pali_len: int = 1

        for right in range(0, n):
            for left in range(right - 1, -1, -1):
                if (right - left == 1 or table[left + 1][right - 1]) \
                        and s[left] == s[right]:
                    table[left][right] = True
                    pali_len = right - left + 1
                    if max_pali_len < pali_len:
                        pali_start = left
                        max_pali_len = pali_len

        return s[pali_start: pali_start + max_pali_len]
