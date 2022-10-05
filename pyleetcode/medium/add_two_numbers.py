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

        stack1: list[int] = []
        stack2: list[int] = []
        while l1 is not None or l2 is not None:
            if l1 is not None:
                stack1.append(l1.val)
                l1 = l1.next
            if l2 is not None:
                stack2.append(l2.val)
                l2 = l2.next

        num1 = sum((n * (10 ** i) for i, n in enumerate(stack1)))
        num2 = sum((n * (10 ** i) for i, n in enumerate(stack2)))

        root = ListNode()
        res = root
        for i in reversed(str(num1 + num2)):
            root.next = ListNode(int(i))
            root = root.next

        return res.next
