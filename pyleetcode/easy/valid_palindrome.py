"""125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def isPalindrome(self, s: str) -> bool:
        s_len = len(s)
        left, right = 0, s_len - 1
        while left <= right and left < s_len and right > 0:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isPalindrome(*args, **kwargs)
