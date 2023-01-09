"""Unit tests of "10. Regular Expression Matching".

https://leetcode.com/problems/regular-expression-matching/
"""

import pytest

from pyleetcode.hard.regular_expression_matching import Solution


TEST_CASES = [
    ('aa', 'a', False),
    ('aa', 'a*', True),
    ('ab', '.*', True),
    ('aab', 'c*a*b', True),
]


@pytest.mark.parametrize('s, p, output', TEST_CASES)
def test(s: str, p: str, output: bool):
    res = Solution().isMatch(s, p)
    assert res == output
