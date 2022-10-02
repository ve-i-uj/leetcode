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
        nodes = []
        root = head
        while root is not None:
            nodes.append(root)
            root = root.next

        root = ListNode()
        node = root
        while nodes:
            node.next = nodes.pop()
            node = node.next
        node.next = None

        return root.next
