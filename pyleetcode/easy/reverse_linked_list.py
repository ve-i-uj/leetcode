"""206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/
"""

from __future__ import annotations

from typing import Optional, List, Any  # noqa: F401


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'

    def __repr__(self) -> str:
        return str(self)


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.reverseList(*args, **kwargs)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        parent = head
        child = head.next
        head = head.next.next
        child.next = parent
        parent.next = None
        while head is not None:
            parent = child
            child = head
            head = head.next
            child.next = parent

        return child
