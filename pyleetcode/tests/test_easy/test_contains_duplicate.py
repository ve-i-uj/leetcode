"""Unit tests of "217. Contains Duplicate".

https://leetcode.com/problems/contains-duplicate/
"""

import pytest

from pyleetcode.easy.contains_duplicate import Solution


TEST_CASES = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
]  # noqa


@pytest.mark.parametrize('nums, expected', TEST_CASES)
def test(nums: list[int], expected: bool):
    actual = Solution().process(nums)
    assert actual is expected
