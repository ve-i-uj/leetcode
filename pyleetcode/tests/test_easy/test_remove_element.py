"""Unit tests of "27. Remove Element".

https://leetcode.com/problems/remove-element/
"""

import pytest

from easy.remove_element import Solution


TEST_CASES = [
    (3, [3, 2, 2, 3], 2, [2, 2]),
    (2, [0, 1, 2, 2, 3, 0, 4, 2], 5, [0, 1, 4, 0, 3]),

    (2, [], 0, []),
]  # noqa


@pytest.mark.parametrize('val, nums, k, expected', TEST_CASES)
def test(val, nums, k, expected):
    res = Solution().process(nums, val)
    assert res == k
    assert sorted(nums[:k]) == sorted(expected[:k])
