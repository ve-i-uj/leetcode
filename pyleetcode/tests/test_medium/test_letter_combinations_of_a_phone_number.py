"""Unit tests of "17. Letter Combinations of a Phone Number".

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

import pytest

from pyleetcode.medium.letter_combinations_of_a_phone_number import Solution


TEST_CASES = [
    ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ('', []),
    ('2', ["a", "b", "c"]),
]


@pytest.mark.parametrize('digits, output', TEST_CASES)
def test(digits: str, output: list[str]):
    res = Solution().process(digits)
    assert res == output
