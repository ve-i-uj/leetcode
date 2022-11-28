"""Unit tests of "3. Longest Substring Without Repeating Characters".

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

import pytest

from pyleetcode.medium.longest_substring_without_repeating_characters import Solution


TEST_CASES = [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    (' ', 1),
    ('dvdf', 3),
    ('abcb', 3),
    ('asjrgapa', 6),
]


@pytest.mark.parametrize('s, output', TEST_CASES)
def test(s, output):
    res = Solution().process(s)
    assert res == output

