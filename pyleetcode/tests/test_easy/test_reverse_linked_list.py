"""Unit tests of "206. Reverse Linked List".

https://leetcode.com/problems/reverse-linked-list/
"""

from typing import Optional
import pytest

from easy.reverse_linked_list import Solution, ListNode


def to_node(lst: list[int]) -> Optional[ListNode]:
    node = ListNode()
    res = node
    for val in lst:
        node.next = ListNode(val)
        node = node.next
    return res.next


def from_node(node: Optional[ListNode]) -> list[int]:
    if node is None:
        return []
    res = []
    while node is not None:
        res.append(node.val)
        node = node.next

    return res


TEST_CASES = [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([], []),
]


@pytest.mark.parametrize('head, output', TEST_CASES)
def test(head: list[int], output: list[int]):
    res = Solution().process(to_node(head))
    assert from_node(res) == output
