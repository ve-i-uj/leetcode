"""2. Add Two Numbers

https://leetcode.com/problems/add-two-numbers/
"""

import itertools
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
        return self.addTwoNumbers(*args, **kwargs)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]
                      ) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        root = ListNode()
        res = root
        the_rest = 0
        while l1 is not None or l2 is not None:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0

            the_rest, digit = divmod((num1 + num2 + the_rest), 10)
            root.next = ListNode(digit)
            root = root.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if the_rest != 0:
            root.next = ListNode(the_rest)

        return res.next
