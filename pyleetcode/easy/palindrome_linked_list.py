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
        root = head
        stack = [root]
        while root.next is not None:
            stack.append(root.next)
            root = root.next

        left = 0
        right = len(stack) - 1
        while left <= right:
            if stack[left].val != stack[right].val:
                return False
            left += 1
            right -= 1
        return True
