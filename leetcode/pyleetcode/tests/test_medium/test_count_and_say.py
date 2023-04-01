"""Unit tests of "38. Count and Say".

https://leetcode.com/problems/count-and-say/
"""

import pytest

from pyleetcode.medium.count_and_say import Solution


TEST_CASES = [
    (1, '1'),
    (4, '1211'),
]


@pytest.mark.parametrize('n, output', TEST_CASES)
def test(n: int, output: str):
    res = Solution().process(n)
    assert res == output
