"""Unit tests of "145. Binary Tree Postorder Traversal".

https://leetcode.com/problems/binary-tree-postorder-traversal/
"""

from typing import Optional
import pytest

from pyleetcode.easy.binary_tree_postorder_traversal import Solution, TreeNode


TEST_CASES = [
    ([1, None, 2, 3], [3, 2, 1]),
    ([], []),
    ([1], [1]),
    ([3, 1, 2], [1, 2, 3]),
]


@pytest.mark.parametrize('vals, expected', TEST_CASES)
def test(vals: list[Optional[int]], expected: list[int]):
    tree = TreeNode.to_tree(vals)
    res = Solution().process(tree)
    assert res == expected
