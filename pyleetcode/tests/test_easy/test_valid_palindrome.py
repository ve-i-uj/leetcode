"""Unit tests of "125. Valid Palindrome".

https://leetcode.com/problems/valid-palindrome/
"""

import pytest

from pyleetcode.easy.valid_palindrome import Solution


TEST_CASES = [
    ('A man, a plan, a canal: Panama', True),
    ('race a car', False),
    (' ', True),
    ('a.', True),
    ('.a', True),
]  # noqa
@pytest.mark.parametrize('s, output', TEST_CASES)
def test(s: str, output: bool):
    assert Solution().process(s) is output
