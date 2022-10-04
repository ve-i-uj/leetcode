"""3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.lengthOfLongestSubstring(*args, **kwargs)

    def lengthOfLongestSubstring(self, s: str) -> int:
        chs = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in chs:
                left = max(left, chs[ch] + 1)
            chs[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len
