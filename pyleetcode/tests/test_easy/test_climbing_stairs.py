"""Unit tests of "70. Climbing Stairs".

https://leetcode.com/problems/climbing-stairs/
"""

import pytest

from pyleetcode.easy.climbing_stairs import Solution


TEST_CASES = [
    (2, 2),
    (3, 3),
    (4, 5),
    (35, 14930352),
    (38, 63245986),
    (44, 1134903170),
    (45, 1836311903),
]  # noqa


@pytest.mark.parametrize('input_, output', TEST_CASES)
def test(input_: int, output: int):
    res = Solution().process(input_)
    assert res == output
