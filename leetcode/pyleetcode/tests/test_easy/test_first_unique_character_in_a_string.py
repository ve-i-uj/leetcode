"""Unit tests of "387. First Unique Character in a String".

https://leetcode.com/problems/first-unique-character-in-a-string/
"""

import pytest

from pyleetcode.easy.first_unique_character_in_a_string import Solution


TEST_CASES = [
    ('leetcode', 0),
    ('loveleetcode', 2),
    ('aabb', -1),
    ('dddccdbba', 8),
]


@pytest.mark.parametrize('s, output', TEST_CASES)
def test(s, output):
    res = Solution().process(s)
    assert res == output
