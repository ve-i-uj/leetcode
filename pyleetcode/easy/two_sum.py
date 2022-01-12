"""Two sum.

https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:  # noqa
        index_by_value = {}
        for i, second in enumerate(nums):
            first = target - second
            if first in index_by_value:
                break
            index_by_value[second] = i
        return [index_by_value[first], i]


def test():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]


if __name__ == '__main__':
    test()
