"""Unit tests of "202. Happy Number".

https://leetcode.com/problems/happy-number/
"""

import pytest

from pyleetcode.easy.happy_number import Solution


TEST_CASES = [
    (19, True),
    (2, False),
    (10, True),
]  # noqa


@pytest.mark.parametrize('n, output', TEST_CASES)
def test(n: int, output: bool):
    res = Solution().process(n)
    assert res is output
