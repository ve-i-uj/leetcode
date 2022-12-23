"""83. Remove Duplicates from Sorted List

https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

from typing import Optional

NO_VALUE = 101


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'

    __repr__ = __str__


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.deleteDuplicates(*args, **kwargs)

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node is not None and node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
                continue
            node = node.next

        return head
