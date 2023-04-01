"""Unit tests of "46. Permutations".

https://leetcode.com/problems/permutations/
"""

import pytest

from pyleetcode.medium.permutations import Solution


TEST_CASES = [
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1], [[1]])
]


@pytest.mark.parametrize('nums, output', TEST_CASES)
def test(nums: list[int], output: list[list[int]]):
    res = Solution().process(nums)
    assert res == output
