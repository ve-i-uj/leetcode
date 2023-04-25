"""Unit tests of "13. Roman to Integer".

https://leetcode.com/problems/roman-to-integer/
"""

import pytest

from pyleetcode.easy.roman_to_integer import Solution


TEST_CASES = [
    ("XIX", 19),
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
]

@pytest.mark.parametrize('roman, output', TEST_CASES)
def test(roman: str, output: int):
    res = Solution().romanToInt(roman)
    assert res == output
