"""15. Three Sum

https://leetcode.com/problems/three-sum/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs) -> List[List[int]]:
        return self.threeSum(*args, **kwargs)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        if len(sorted_nums) < 3:
            return []

        res = set()

        if sorted_nums[0] > 0 or sorted_nums[-1] < 0:
            return []

        for i in range(len(sorted_nums)):
            left, right = i + 1, len(sorted_nums) - 1
            while left < right:
                s = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if s == 0:
                    res.add(tuple(sorted([sorted_nums[i], sorted_nums[left], sorted_nums[right]])))
                    left += 1

                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]:
                        right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1

        return list(list(t) for t in res)
