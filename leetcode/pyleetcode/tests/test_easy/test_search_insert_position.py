"""Unit tests of "35. Search Insert Position".

https://leetcode.com/problems/search-insert-position/
"""

import pytest

from pyleetcode.easy.search_insert_position import Solution


TEST_CASES = [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1], 1, 0),
    ([1, 3], 1, 0),
]  # noqa


@pytest.mark.parametrize('nums, target, output', TEST_CASES)
def test(nums: list[int], target: int, output: int):
    res = Solution().process(nums, target)
    assert res == output
