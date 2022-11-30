"""Unit tests of "22. Generate Parentheses".

https://leetcode.com/problems/generate-parentheses/
"""

import pytest

from pyleetcode.medium.generate_parentheses import Solution


TEST_CASES = [
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (1, ["()"]),
    # (6, []),
]


@pytest.mark.parametrize('n, output', TEST_CASES)
def test(n: int, output: list[str]):
    res = Solution().process(n)
    assert sorted(res) == sorted(output)
