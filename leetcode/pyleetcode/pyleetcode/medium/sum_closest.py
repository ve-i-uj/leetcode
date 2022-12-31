"""16. 3Sum Closest

https://leetcode.com/problems/sum-closest/
"""

from typing import List


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        nums.sort()
        res: int = sum(nums[:3])
        for i, _n in enumerate(nums):
            l, r = i - 1, i + 1
            while l >= 0 and r < len(nums):
                s = nums[i] + nums[l] + nums[r]
                res, _ = min(
                    (res, abs(target - res)),
                    (s, abs(target - s)),
                    key=lambda t: t[1]
                )

                if res == target:
                    return res

                if s > target:
                    l -= 1
                else:
                    r += 1

        return res
