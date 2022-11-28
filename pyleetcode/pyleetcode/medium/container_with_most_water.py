"""11. Container With Most Water

https://leetcode.com/problems/container-with-most-water/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs) -> int:
        return self.maxArea(*args, **kwargs)

    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height):
                if i == j:
                    continue

                res = max(res, (j - i) * min(h1, h2))

        return res
