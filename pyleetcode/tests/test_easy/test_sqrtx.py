"""Unit tests of "69. Sqrtx".

https://leetcode.com/problems/sqrtx/
"""

import pytest

from easy.sqrtx import Solution


TEST_CASES = [
    (4, 2),
    (8, 2),
    (0, 0),
    (2, 1),
    (9, 3),
    (2147395599, 46339),
]  # noqa


@pytest.mark.parametrize('input_, output', TEST_CASES)
def test(input_: int, output: int):
    res = Solution().process(input_)
    assert res == output
