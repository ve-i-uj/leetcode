"""Unit tests of "2. Add Two Numbers".

https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional

import pytest

from medium.add_two_numbers import Solution, ListNode


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
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
]


@pytest.mark.parametrize('l1, l2, output', TEST_CASES)
def test(l1, l2, output):
    res = Solution().process(to_node(l1), to_node(l2))
    assert from_node(res) == output
