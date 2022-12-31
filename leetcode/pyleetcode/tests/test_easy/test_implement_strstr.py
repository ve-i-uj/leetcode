"""Unit tests of "28. Implement strStr".

https://leetcode.com/problems/implement-strstr/
"""

import pytest

from pyleetcode.easy.implement_strstr import Solution


TEST_CASES = [
    ('hello', 'll', 2),
    ('aaaaa', 'bba', -1),
    ('', 'any', -1),
    ('any', '', 0),
]


@pytest.mark.parametrize('haystack, needle, expected', TEST_CASES)
def test(haystack: str, needle: str, expected: int):
    res = Solution().process(haystack, needle)
    assert res == expected
