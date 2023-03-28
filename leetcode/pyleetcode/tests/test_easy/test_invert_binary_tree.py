"""Unit tests of "226. Invert Binary Tree".

https://leetcode.com/problems/invert-binary-tree/
"""

import pytest

from pyleetcode.easy.invert_binary_tree import Solution, TreeNode


TEST_CASES = [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], []),
]


@pytest.mark.parametrize('root, output', TEST_CASES)
def test(root: list[int], output: list[int]):
    res = Solution().process(TreeNode.to_tree(root))
    lst = TreeNode.from_tree(res)
    assert lst == output
