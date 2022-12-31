"""Unit tests of "1207. Unique Number of Occurrences".

https://leetcode.com/problems/unique-number-of-occurrences/
"""

import pytest

from pyleetcode.easy.unique_number_of_occurrences import Solution


TEST_CASES = [
    ([1, 2, 2, 1, 1, 3], True),
    ([1, 2], False),
    ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
]


@pytest.mark.parametrize('arr, output', TEST_CASES)
def test(arr: list[int], output: bool):
    res = Solution().process(arr)
    assert res is output
