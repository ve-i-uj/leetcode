"""Unit tests of "94. Binary Tree Inorder Traversal".

https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

import pytest

from easy.binary_tree_inorder_traversal import Solution, TreeNode


TEST_CASES = [
    ([1, None, 2, 3], [1, 3, 2]),
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4], [4, 2, 1, 3]),
    ([1, 2, 3, 4, 5, None, 7], [4, 2, 5, 1, 3, 7]),
]  # noqa


@pytest.mark.parametrize('input_, output', TEST_CASES)
def test(input_: list[int], output: list[int]):
    TreeNode.normalize_data(input_)
    tree = TreeNode.new(input_)
    res = Solution().process(tree)
    assert res == output
