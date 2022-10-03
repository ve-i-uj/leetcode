"""3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.lengthOfLongestSubstring(*args, **kwargs)

    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chs = set()
        for i in range(len(s)):
            for ch in s[i:]:
                if ch in chs:
                    res = max(res, len(chs))
                    break
                else:
                    chs.add(ch)

            res = max(res, len(chs))
            chs.clear()

            for ch in s[:i]:
                if ch in chs:
                    res = max(res, len(chs))
                    break
                else:
                    chs.add(ch)

            res = max(res, len(chs))
            chs.clear()

        return res
