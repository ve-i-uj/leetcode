"""11. Container With Most Water

https://leetcode.com/problems/container-with-most-water/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs) -> int:
        return self.maxArea(*args, **kwargs)

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
