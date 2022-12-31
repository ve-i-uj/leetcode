"""Unit tests of "112. Path Sum".

https://leetcode.com/problems/path-sum/
"""

from typing import Optional
import pytest

from pyleetcode.easy.path_sum import Solution, TreeNode


TEST_CASES = [
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
    ([1, 2, 3], 5, False),
    ([], 0, False),
    ([1, 2], 1, False),
    ([-2, None, -3], -5, True),
]


@pytest.mark.parametrize('root, targetSum, output', TEST_CASES)
def test(root: list[Optional[int]], targetSum: int, output: bool):
    res = Solution().process(TreeNode.create(root), targetSum)
    assert res == output
