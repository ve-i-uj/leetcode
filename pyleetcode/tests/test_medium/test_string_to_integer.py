"""Unit tests of "8. String to Integer".

https://leetcode.com/problems/string-to-integer/
"""

import pytest

from pyleetcode.medium.string_to_integer import Solution


TEST_CASES = [
    ('42', 42),
    ('   -42', -42),
    ('4193 with words', 4193),
]  # noqa


@pytest.mark.parametrize('s, output', TEST_CASES)
def test(s: str, output: int):
    res = Solution().process(s)
    assert res == output
