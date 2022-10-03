"""Unit tests of "234. Palindrome Linked List".

https://leetcode.com/problems/palindrome-linked-list/
"""

import pytest
from typing import Optional

from easy.palindrome_linked_list import Solution, ListNode


TEST_CASES = [
    ([1, 2, 2, 1], True),
    ([1, 2], False),
    ([1, 2, 3, 2, 1], True),
]


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


@pytest.mark.parametrize('nums, output', TEST_CASES)
def test(nums: list[int], output: bool):
    res = Solution().process(to_node(nums))
    assert res is output
