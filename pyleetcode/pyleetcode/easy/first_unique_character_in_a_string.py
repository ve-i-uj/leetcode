"""387. First Unique Character in a String

https://leetcode.com/problems/first-unique-character-in-a-string/
"""

import collections
from dataclasses import dataclass
from typing import Optional, List, Any  # noqa: F401


@dataclass
class Info:
    index: int
    char: str
    cntr: int = 0


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.firstUniqChar(*args, **kwargs)

    def firstUniqChar(self, s: str) -> int:
        table = collections.OrderedDict()
        for i, ch in enumerate(s):
            new_info = Info(i, ch, 1)
            info: Info = table.setdefault(ch, new_info)
            if info is not new_info:
                info.cntr += 1

        for info in table.values():
            if info.cntr == 1:
                return info.index

        return -1
