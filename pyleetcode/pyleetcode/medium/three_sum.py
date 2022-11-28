"""15. Three Sum

https://leetcode.com/problems/three-sum/
"""

from typing import Optional, List, Any  # noqa: F401


class Solution:

    def process(self, *args, **kwargs) -> List[List[int]]:
        return self.threeSum(*args, **kwargs)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = set()
        for i in range(length):
            for j in range(length):
                if j == i:
                    continue
                for k in range(length):
                    if k == j or k == i:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return list(list(t) for t in res)
