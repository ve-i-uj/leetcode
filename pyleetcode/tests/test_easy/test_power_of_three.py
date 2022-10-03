"""Unit tests of "326. Power of Three".

https://leetcode.com/problems/power-of-three/
"""

import pytest

from easy.power_of_three import Solution


TEST_CASES = [
    (27, True),
    (0, False),
    (-1, False),
    (45, False),
    (-3, False),
    (-9, False),
    (-27, False),
]


@pytest.mark.parametrize('n, output', TEST_CASES)
def test(n: int, output: str):
    res = Solution().process(n)
    assert res is output
