"""160. Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/
"""
from __future__ import annotations

from typing import Optional, List, Any  # noqa: F401


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(intersectVal: int, listA: list[int], listB: list[int],
               skipA: int, skipB: int) -> tuple[ListNode, ListNode, ListNode]:
        stack_a = []
        stack_b = []
        for v in listA:
            stack_a.append(ListNode(v))
        for v in listB:
            stack_b.append(ListNode(v))
        if len(stack_a) > len(stack_b):
            stack_a[skipA:] = stack_b[skipB:]
        else:
            stack_b[skipB:] = stack_a[skipA:]

        common_node = None
        if stack_a[skipA:skipA + 1]:
            common_node = stack_a[skipA:skipA + 1][0]

        node = stack_a.pop(0)
        head_a = node
        while stack_a:
            node.next = stack_a.pop(0)
            node = node.next

        node = stack_b.pop(0)
        head_b = node
        while stack_b:
            node.next = stack_b.pop(0)
            node = node.next

        return head_a, head_b, common_node


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode
                            ) -> Optional[ListNode]:
        ptr1 = headA
        ptr2 = headB
        while ptr1 is not ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

            if ptr1 is ptr2:
                return ptr1

            if ptr1 is None:
                ptr1 = headB
            if ptr2 is None:
                ptr2 = headA

        return ptr1

    def process(self, *args, **kwargs):
        return self.getIntersectionNode(*args, **kwargs)
