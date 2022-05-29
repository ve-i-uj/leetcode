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
        common_node = None

        node = ListNode(listA[0])
        headA = node
        i = 2
        common_node = None
        while i <= len(listA):
            node.next = ListNode(listA[i - 1])
            node = node.next
            if i > skipA and common_node is None:
                common_node = node
            i += 1

        node = ListNode(listB[0])
        headB = node
        i = 2
        while i <= skipB and i <= len(listB):
            node.next = ListNode(listB[i - 1])
            node = node.next
            i += 1
        if common_node is not None:
            node.next = common_node

        return headA, headB, common_node


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stack_a: list[ListNode] = []
        stack_b: list[ListNode] = []
        node = headA
        while node is not None:
            stack_a.append(node)
            node = node.next
        node = headB
        while node is not None:
            stack_b.append(node)
            node = node.next

        last_node = None
        for node_a, node_b in zip(reversed(stack_a), reversed(stack_b)):
            if node_a is not node_b:
                break
            last_node = node_a

        return last_node

    def process(self, *args, **kwargs):
        return self.getIntersectionNode(*args, **kwargs)
