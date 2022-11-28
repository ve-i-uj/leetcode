"""Unit tests of "15. Three Sum".

https://leetcode.com/problems/three-sum/
"""

import pytest

from pyleetcode.medium.three_sum import Solution


TEST_CASES = [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
    ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
]


@pytest.mark.parametrize('nums, output', TEST_CASES)
def test(nums: list[int], output: list[list[int]]):
    res = Solution().process(nums)
    assert sorted(res) == sorted(output)
