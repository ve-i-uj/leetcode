"""Unit tests of "7. Reverse Integer".

https://leetcode.com/problems/reverse-integer/
"""

import pytest

from medium.reverse_integer import Solution


TEST_CASES = [
    (123, 321),
    (-123, -321),
    (120, 21),
    (0, 0),
    (1534236469, 0),
]  # noqa


@pytest.mark.parametrize('x, output', TEST_CASES)
def test(x, output):
    res = Solution().process(x)
    assert res == output
