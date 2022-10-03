"""234. Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/
"""

from typing import Optional, List, Any  # noqa: F401

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'

    def __repr__(self) -> str:
        return str(self)


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isPalindrome(*args, **kwargs)

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        fp = head
        sp = head
        while fp is not None and fp.next is not None:
            sp: ListNode = sp.next  # type: ignore
            fp = fp.next.next

        p1: Optional[ListNode] = None
        p2: ListNode = sp
        p3: Optional[ListNode] = sp.next
        p2.next = p1
        while p3 is not None:
            p1 = p2
            p2 = p3
            p3 = p3.next

            p2.next = p1

        head2 = p2

        while head2 is not None:
            if head.val != head2.val:
                return False

            head = head.next
            head2 = head2.next

        return True


