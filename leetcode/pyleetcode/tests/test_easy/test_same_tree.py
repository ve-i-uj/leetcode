"""Unit tests of "100. Same Tree".

https://leetcode.com/problems/same-tree/
"""

from typing import Optional
import pytest

from pyleetcode.easy.same_tree import Solution, TreeNode


TEST_CASES = [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False),
]


def to_node(lst: list[Optional[int]]) -> Optional[TreeNode]:

    def create_node(i: int, lst: list[Optional[int]]):
        if i >= len(lst):
            return

        val = lst[i]
        if val is None:
            return

        node = TreeNode(val)
        node.left = create_node(i * 2 + 1, lst)
        node.left = create_node(i * 2 + 2, lst)

        return node

    return create_node(0, lst)


@pytest.mark.parametrize('p, q, output', TEST_CASES)
def test(p: list[Optional[int]], q: list[Optional[int]], output: bool):
    res = Solution().process(to_node(p), to_node(q))
    assert res == output
