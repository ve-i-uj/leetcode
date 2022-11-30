"""19. Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Optional, List, Any  # noqa: F401


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def process(self, *args, **kwargs):
        return self.removeNthFromEnd(*args, **kwargs)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int    # noqa: N802
                         ) -> Optional[ListNode]:
        res = ListNode()
        res.next = head

        first: ListNode = ListNode(0, next=res)
        second = res.next

        i = 0
        while second is not None:
            i += 1
            if i >= n:
                assert first.next is not None
                first = first.next

            second = second.next

        if first.next is not res:
            parent = first
            nth_node = parent.next
            assert nth_node is not None
            parent.next = nth_node.next

        return res.next
