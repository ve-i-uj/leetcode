"""5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.longestPalindrome(*args, **kwargs)

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        n = len(s)
        table: dict[tuple[int, int], bool] = {}
        max_pali = s[0]

        def is_pali(left: int, right: int) -> bool:
            if (left, right) in table:
                return table[(left, right)]

            if left == right and s[left] == s[right]:
                # a
                table[(left, right)] = True
            elif right - left == 1 and s[left] == s[right]:
                # aa
                table[(left, right)] = True
            elif right - left > 1 and s[left] == s[right] \
                    and is_pali(left + 1, right - 1):
                # "aba" and "abba"
                table[(left, right)] = True
            else:
                table[(left, right)] = False

            return table[(left, right)]

        left = 0
        for right, ch in enumerate(s):
            for left in range(right - 1, -1, -1):
                if is_pali(left, right):
                    max_pali = max(max_pali, s[left: right + 1], key=len)

        return max_pali
