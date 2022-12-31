"""Unit tests of "242. Valid Anagram".

https://leetcode.com/problems/valid-anagram/
"""

import pytest

from pyleetcode.easy.valid_anagram import Solution


TEST_CASES = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("aa", "a", False),
]


@pytest.mark.parametrize('s, t, output', TEST_CASES)
def test(s: str, t: str, output: bool):
    res = Solution().process(s, t)
    assert res is output
