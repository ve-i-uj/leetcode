"""Unit tests of "111. Minimum Depth of Binary Tree".

https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

from typing import Optional
import pytest

from pyleetcode.easy.minimum_depth_of_binary_tree import Solution, TreeNode


TEST_CASES = [
    ([3, 9, 20, None, None, 15, 7], 2),
    ([2, None, 3, None, 4, None, 5, None, 6], 5),
]


@pytest.mark.parametrize('root, output', TEST_CASES)
def test(root: list[Optional[int]], output: int):
    res = Solution().process(TreeNode.create(root))
    assert res == output
