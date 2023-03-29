"""Unit tests of "543. Diameter of Binary Tree".

https://leetcode.com/problems/diameter-of-binary-tree/
"""

import pytest

from pyleetcode.easy.diameter_of_binary_tree import Solution, TreeNode


TEST_CASES = [
    ([1, 2, 3, 4, 5], 3),
    ([1, 2], 1),
    ([1], 0),
    ([2, 3, None, 1], 2),
]


@pytest.mark.parametrize('root, output', TEST_CASES)
def test(root: list[int], output: int):
    res = Solution().process(TreeNode.to_tree(root))
    assert output == res
