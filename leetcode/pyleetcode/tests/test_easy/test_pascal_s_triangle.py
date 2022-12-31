"""Unit tests of "118. Pascal's Triangle".

https://leetcode.com/problems/pascal-s-triangle/
"""

import pytest

from pyleetcode.easy.pascal_s_triangle import Solution


TEST_CASES = [
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    (1, [[1]]),
]


@pytest.mark.parametrize('num_rows, output', TEST_CASES)
def test(num_rows: int, output: list[list[int]]):
    res = Solution().process(num_rows)
    assert res == output
