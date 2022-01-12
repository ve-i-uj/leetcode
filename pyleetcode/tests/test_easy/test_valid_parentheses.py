"""Unit tests of `20. Valid Parentheses`.

https://leetcode.com/problems/valid-parentheses/
"""

import pytest

from easy.valid_parentheses import Solution, TEST_CASES


@pytest.mark.parametrize("s,res", TEST_CASES.items())
def test_1(s: str, res: bool):
    assert Solution().isValid(s) is res
