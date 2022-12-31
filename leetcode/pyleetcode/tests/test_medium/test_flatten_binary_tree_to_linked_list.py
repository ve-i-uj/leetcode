"""Unit tests of "114. Flatten Binary Tree to Linked List".

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

from typing import Optional
import pytest

from pyleetcode.medium.flatten_binary_tree_to_linked_list import Solution, TreeNode


TEST_CASES = [
    ([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
    ([], []),
    ([0], [0]),
]


@pytest.mark.parametrize('root, output', TEST_CASES)
def test(root: list[Optional[int]], output: list[Optional[int]]):
    tree = TreeNode.create(root)
    Solution().process(tree)

    res = []
    while tree is not None:
        res.append(tree.val)
        res.append(None)
        tree = tree.right

    res = res[:-1]
    assert res == output
