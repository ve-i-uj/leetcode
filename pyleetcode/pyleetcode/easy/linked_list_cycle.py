"""141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/
"""
from __future__ import annotations

from typing import Optional, List, Any  # noqa: F401


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create_tree(vals: list[int], cycle_pos: int) -> Optional[ListNode]:
        if not vals:
            return None
        root = ListNode(vals[0])
        nodes: list[ListNode] = [root]
        for v in vals[1:]:
            node = ListNode(v)
            nodes[-1].next = node
            nodes.append(node)
        if cycle_pos >= 0:
            nodes[-1].next = nodes[cycle_pos]

        return root


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True

        return False

    def process(self, *args, **kwargs):  # noqa: N802
        return self.hasCycle(*args, **kwargs)
