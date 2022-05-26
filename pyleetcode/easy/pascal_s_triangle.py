"""118. Pascal's Triangle

https://leetcode.com/problems/pascal-s-triangle/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        last = []
        for n in range(numRows):
            for i in reversed(range(1, n)):
                last[i] += last[i - 1]
            last.append(1)
            res.append(last[:])
        return res

    def process(self, *args, **kwargs):  # noqa: N802
        return self.generate(*args, **kwargs)
