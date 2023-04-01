"""46. Permutations

https://leetcode.com/problems/permutations/
"""

import itertools
from typing import List


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.permute(*args, **kwargs)

    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in itertools.permutations(nums, len(nums))]