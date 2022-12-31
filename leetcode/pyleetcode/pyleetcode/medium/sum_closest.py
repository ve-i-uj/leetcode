"""16. 3Sum Closest

https://leetcode.com/problems/sum-closest/
"""

from typing import List


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        res: int = sum(nums[:3])
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums[1:], start=1):
                for k, n3 in enumerate(nums[2:], start=2):
                    if i == j or i == k or j == k:
                        continue
                    s = n1 + n2 + n3
                    if s == target:
                        return s
                    (_value, res) = min(
                        (abs(target - res), res),
                        (abs(target - s), s),
                        key=lambda t: t[0]
                    )

        return res
