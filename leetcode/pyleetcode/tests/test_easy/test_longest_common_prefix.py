"""Unit tests of 14. Longest Common Prefix.

https://leetcode.com/problems/longest-common-prefix/
"""

import pytest

from pyleetcode.easy.longest_common_prefix import Solution


TEST_CASES = [
    (['flower', 'flow', 'flight'], 'fl'),
    (['dog', 'disk', 'doom'], 'd'),
    (['dog', '', 'doom'], ''),
    (['dog', 'racecar', 'car'], ''),

    ([''], ''),
    (['a'], 'a'),
    (['reflower', 'flow', 'flight'], ''),
    (['ab', 'a'], 'a'),
    (['flower', 'flower', 'flower', 'flower'], 'flower'),

]


@pytest.mark.parametrize('strs,res', TEST_CASES)
def test_1(strs: list[str], res: bool):
    assert Solution().process(strs) == res
