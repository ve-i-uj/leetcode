"""15. Three Sum

https://leetcode.com/problems/three-sum/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs) -> List[List[int]]:
        return self.threeSum(*args, **kwargs)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = set()

        for i in range(len(sorted_nums)):
            left, right = i + 1, len(sorted_nums) - 1
            while left < right:
                s = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if s == 0:
                    res.add(tuple(sorted([sorted_nums[i], sorted_nums[left], sorted_nums[right]])))
                if s > 0:
                    right -= 1
                else:
                    left += 1

        return list(list(t) for t in res)
