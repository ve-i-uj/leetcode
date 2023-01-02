"""Unit tests of 21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/
"""

import pytest

from pyleetcode.easy.merge_two_sorted_lists import Solution, to_node, ListNode, \
    ExtListNode


TEST_CASES = [
    (to_node([1, 2, 4], ExtListNode), to_node([1, 3, 4], ExtListNode),
     to_node([1, 1, 2, 3, 4, 4], ExtListNode)),
    (None, None, None),
    (None, to_node([0], ExtListNode), to_node([0], ExtListNode)),
    (to_node([5], ExtListNode), to_node([1, 2, 6], ExtListNode),
     to_node([1, 2, 5, 6], ExtListNode)),

    (to_node([5], ExtListNode), to_node([1, 2, 4], ExtListNode),
     to_node([1, 2, 4, 5], ExtListNode)),
    (to_node([-2, 5], ExtListNode), to_node([-9, -6, -3, -1, 1, 6], ExtListNode),
     to_node([-9, -6, -3, -2, -1, 1, 5, 6], ExtListNode)),
    (to_node([1], ExtListNode), to_node([1], ExtListNode),
     to_node([1, 1], ExtListNode)),
    (to_node([-10, -9, -6, -4, 1, 9, 9], ExtListNode),
     to_node([-5, -3, 0, 7, 8, 8], ExtListNode),
     to_node([-10, -9, -6, -5, -4, -3, 0, 1, 7, 8, 8, 9, 9], ExtListNode)),
]


@pytest.mark.parametrize('list1, list2, res', TEST_CASES)
def test_1(list1: ListNode, list2: ListNode, res: list):
    assert ExtListNode.cast(Solution().process(list1, list2)) == res
