"""Unit tests of "119. Pascal's Triangle II".

https://leetcode.com/problems/pascals-triangle-ii/
"""

import pytest

from pyleetcode.easy.pascals_triangle_ii import Solution


TEST_CASES = [
    (3, [1, 3, 3, 1]),
    (0, [1]),
    (1, [1, 1]),
]


@pytest.mark.parametrize('rowIndex, expected', TEST_CASES)
def test(rowIndex: int, expected: list[int]):
    res = Solution().process(rowIndex)
    assert expected == res
