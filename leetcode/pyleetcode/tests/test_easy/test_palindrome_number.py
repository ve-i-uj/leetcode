"""Unit tests of "234. Palindrome Linked List".

https://leetcode.com/problems/palindrome-linked-list/
"""

import pytest
from typing import Optional

from pyleetcode.easy.palindrome_number import Solution


TEST_CASES = [
    (121, True),
    (-121, False),
    (10, False),
    (0, True),
]

@pytest.mark.parametrize('x, output', TEST_CASES)
def test(x: int, output: bool):
    res = Solution().isPalindrome(x)
    assert res is output
