"""Unit tests of "110. Balanced Binary Tree".

https://leetcode.com/problems/balanced-binary-tree/
"""

from typing import Optional
import pytest

from pyleetcode.easy.balanced_binary_tree import Solution, TreeNode


TEST_CASES = [
    ([3, 9, 20, None, None, 15, 7], True),
    ([1, 2, 2, 3, 3, None, None, 4, 4], False),
    ([], True),
]


@pytest.mark.parametrize('root, output', TEST_CASES)
def test(root: list[Optional[int]], output: bool):
    res = Solution().process(TreeNode.new(root))
    assert res == output
