"""171. Excel Sheet Column Number

https://leetcode.com/problems/excel-sheet-column-number/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def titleToNumber(self, columnTitle: str) -> int:
        # res = 0
        # for i, ch in enumerate(reversed(columnTitle)):
        #     res += (26 ** i) * (ord(ch) - 64)
        # return res
        return sum(((26 ** i) * (ord(ch) - 64) for i, ch
                    in enumerate(reversed(columnTitle))), 0)

    def process(self, *args, **kwargs):  # noqa: N802
        return self.titleToNumber(*args, **kwargs)
