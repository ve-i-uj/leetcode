"""Unit tests of "19. Remove Nth Node From End of List".

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Optional

import pytest

from pyleetcode.medium.remove_nth_node_from_end_of_list import Solution, ListNode


TEST_CASES = [
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1], 1, []),
    ([1, 2], 1, [1]),
]


def to_node(lst: list[int]) -> Optional[ListNode]:
    if not lst:
        return None
    node = ListNode(lst[0])
    node.next = to_node(lst[1:])
    return node


def to_list(node: Optional[ListNode]) -> list:
    if node is None:
        return []
    return [node.val] + to_list(node.next)


@pytest.mark.parametrize('head, n, output', TEST_CASES)
def test(head: list[int], n: int, output: list[int]):
    root = to_node(head)
    res = Solution().process(root, n)
    assert output == to_list(res)
