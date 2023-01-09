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
    ('ab', 'c*a*b', True),
    ('cb', 'c*a*b', True),
    ('mississippi', 'mis*is*p*.', False),
    ('ab', '.*c', False),
    ('aaa', 'aaaa', False),
    ('aaa', 'a*a', True),
    ('a', 'ab*', True),
    ('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c', False),
    ('mississippi', 'mis*is*ip*.', True),
    ('aa', 'aa', True),
    ('a', 'b', False),
    ('a', '.*..a*', False),
    ('bbab', 'b*a*', False),
    ('bbba', '.*b', False),
    ('acaabbaccbbacaabbbb', 'a*.*b*.*a*aa*a*', False),
    ('abcaaaaaaabaabcabac', '.*ab.a.*a*a*.*b*b*', True),
]


@pytest.mark.parametrize('s, p, output', TEST_CASES)
def test(s: str, p: str, output: bool):
    res = Solution().isMatch(s, p)
    assert res == output
