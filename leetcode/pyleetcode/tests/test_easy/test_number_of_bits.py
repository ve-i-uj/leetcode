"""Unit tests of "191. Number of 1 Bits".

https://leetcode.com/problems/number-of-bits/
"""

import pytest

from pyleetcode.easy.number_of_bits import Solution


TEST_CASES = [
    (int('00000000000000000000000000001011', 2), 3),
    (int('00000000000000000000000010000000', 2), 1),
    (int('11111111111111111111111111111101', 2), 31),
]  # noqa


@pytest.mark.parametrize('n, output', TEST_CASES)
def test(n: int, output: int):
    res = Solution().process(n)
    assert res == output
