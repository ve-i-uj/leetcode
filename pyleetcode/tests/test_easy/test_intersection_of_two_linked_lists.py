"""Unit tests of "160. Intersection of Two Linked Lists".

https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

import pytest

from easy.intersection_of_two_linked_lists import Solution, ListNode


TEST_CASES = [
    (8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3),
    (2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1),
    (0, [2, 6, 4], [1, 5], 3, 2),
]


@pytest.mark.parametrize('intersectVal, listA, listB, skipA, skipB', TEST_CASES)
def test(intersectVal: int, listA: list[int], listB: list[int], skipA: int, skipB: int):
    list_a, list_b, common_node = ListNode.create(
        intersectVal, listA, listB, skipA, skipB)
    res = Solution().process(list_a, list_b)
    assert res is common_node
