"""28. Implement strStr

https://leetcode.com/problems/implement-strstr/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.strStr(*args, **kwargs)

    def strStr(self, haystack: str, needle: str) -> int:  # noqa: N802
        if not needle:
            return 0
        return haystack.find(needle)
