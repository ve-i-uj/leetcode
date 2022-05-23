"""Unit tests of "104. Maximum Depth of Binary Tree".

https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

from typing import Optional
import pytest

from easy.maximum_depth_of_binary_tree import Solution, TreeNode


TEST_CASES = [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2),
    ([], 0),
]  # noqa


def create_root(vals: list[Optional[int]]) -> Optional[TreeNode]:

    def create(i) -> Optional[TreeNode]:
        if i >= len(vals):
            return None
        node = TreeNode(vals[i])
        node.left = create(i * 2 + 1)
        node.right = create(i * 2 + 2)
        return node

    if not vals:
        return None

    return create(0)


@pytest.mark.parametrize('vals, output', TEST_CASES)
def test(vals: list[Optional[int]], output: int):
    res = Solution().process(create_root(vals))
    assert res == output
