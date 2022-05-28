"""Unit tests of "141. Linked List Cycle".

https://leetcode.com/problems/linked-list-cycle/
"""

import pytest

from easy.linked_list_cycle import Solution, ListNode


TEST_CASES = [
    ([3, 2, 0, -4], 1, True),
    ([1, 2], 0, True),
    ([1], -1, False),
]


@pytest.mark.parametrize('vals, pos, output', TEST_CASES)
def test(vals: list[int], pos: int, output: bool):
    head = ListNode.create_tree(vals, pos)
    res = Solution().process(head)
    assert res == output
