"""Unit tests of "344. Reverse String".

https://leetcode.com/problems/reverse-string/
"""

import pytest

from easy.reverse_string import Solution


TEST_CASES = [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]),
    ([], []),
]  # noqa


@pytest.mark.parametrize('s, res', TEST_CASES)
def test(s: list[str], res: list[str]):
    Solution().process(s)
    assert s == res
