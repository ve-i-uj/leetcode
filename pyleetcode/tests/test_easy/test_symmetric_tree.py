"""Unit tests of "101. Symmetric Tree".

https://leetcode.com/problems/symmetric-tree/
"""

from typing import Optional
import pytest

from pyleetcode.easy.symmetric_tree import Solution, TreeNode


TEST_CASES = [
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False),
]  # noqa


@pytest.mark.parametrize('vals, output', TEST_CASES)
def test(vals: list[Optional[int]], output: bool):
    root = TreeNode.new(vals)
    res = Solution().process(root)
    assert res == output
