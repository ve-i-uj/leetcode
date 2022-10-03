"""242. Valid Anagram

https://leetcode.com/problems/valid-anagram/
"""

import collections
from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isAnagram(*args, **kwargs)

    def isAnagram(self, s: str, t: str) -> bool:
        s_ctr = collections.Counter(s)
        t_ctr = collections.Counter(t)

        return s_ctr == t_ctr

