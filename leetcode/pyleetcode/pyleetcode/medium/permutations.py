"""46. Permutations

https://leetcode.com/problems/permutations/
"""

import itertools
from typing import List


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.permute(*args, **kwargs)

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        res = []
        for _ in range(len(nums)):
            head, *nums = nums[:]
            perms = self.permute(nums)

            for perm in perms:
                perm.append(head)

            nums.append(head)
            res.extend(perms)

        return res

