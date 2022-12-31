"""Unit tests of "113. Path Sum II".

https://leetcode.com/problems/path-sum-ii/
"""

from typing import Optional
import pytest

from pyleetcode.medium.path_sum_ii import Solution, TreeNode


TEST_CASES = [
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, [[5, 4, 11, 2], [5, 8, 4, 5]]),
    ([1, 2, 3], 5, []),
    ([1, 2], 0, []),
]


@pytest.mark.parametrize('root, targetSum, output', TEST_CASES)
def test(root: list[Optional[int]], targetSum: int, output: list[list[int]]):
    res = Solution().process(TreeNode.create(root), targetSum)
    assert sorted(res) == sorted(output)
