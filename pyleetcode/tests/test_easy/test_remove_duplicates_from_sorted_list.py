"""Unit tests of "83. Remove Duplicates from Sorted List".

https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

from typing import Optional
import pytest

from pyleetcode.easy.remove_duplicates_from_sorted_list import Solution, ListNode


TEST_CASES = [
    ([1, 1, 2], [1, 2]),
    ([1, 1, 2, 3, 3], [1, 2, 3]),
]


def to_node(lst: list[int]) -> Optional[ListNode]:
    root = ListNode()
    res = root
    for n in lst:
        root.next = ListNode(n)
        root = root.next
    return res.next


def from_node(node: Optional[ListNode]) -> list[int]:
    res = []
    while node is not None:
        res.append(node.val)
        node = node.next
    return res


@pytest.mark.parametrize('head, output', TEST_CASES)
def test(head: list[int], output: list[int]):
    res = Solution().process(to_node(head))
    assert from_node(res) == output
