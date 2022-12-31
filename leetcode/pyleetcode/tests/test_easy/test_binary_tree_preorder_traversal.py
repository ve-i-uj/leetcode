"""Unit tests of "144. Binary Tree Preorder Traversal".

https://leetcode.com/problems/binary-tree-preorder-traversal/
"""

from typing import Optional
import pytest

from pyleetcode.easy.binary_tree_preorder_traversal import Solution, TreeNode


TEST_CASES = [
    ([1, None, 2, 3], [1, 2, 3]),
    ([], []),
    ([1], [1]),
]


@pytest.mark.parametrize('root, output', TEST_CASES)
def test(root: list[Optional[int]], output: list[int]):
    res = Solution().process(TreeNode.create(root))
    assert res == output
