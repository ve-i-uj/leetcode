"""119. Pascal's Triangle II

https://leetcode.com/problems/pascals-triangle-ii/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.getRow(*args)

    def getRow(self, rowIndex: int) -> List[int]:
        last = []
        for n in range(rowIndex + 1):
            for i in reversed(range(1, n)):
                last[i] += last[i - 1]
            last.append(1)

        return last
