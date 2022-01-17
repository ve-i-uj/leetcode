"""21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/
"""

import bisect

from typing import Optional, List, Any


# Definition for singly-linked list.

class ListNode:

    def __init__(self, val=0, next=None):  # noqa
        self.val = val
        self.next = next


class ExtListNode(ListNode):

    def __str__(self) -> str:
        return str(to_list(self))

    def __repr__(self):
        return str(self)

    def __eq__(self, __o: Any) -> bool:
        res = to_list(self) == to_list(__o)
        return res

    @classmethod
    def cast(cls, node: ListNode) -> 'ExtListNode':
        if node is None:
            return None
        lst = to_list(node)
        ext_node = to_node(lst, ExtListNode)
        return ext_node


def to_list(node: ListNode) -> List:
    res = []
    res.append(node.val)
    while node.next is not None:
        node = node.next
        res.append(node.val)

    return res


def to_node(lst: List, node_class=ListNode) -> ListNode:
    last_node = node_class(val=lst.pop(), next=None)
    for val in reversed(lst):
        last_node = node_class(val=val, next=last_node)

    return last_node


def merge(lst1: list, lst2: list) -> list:
    res = []
    for i, j in zip(lst1, lst2):
        if i == j:
            continue
        if i < j:
            to_lst = lst1
            from_lst = lst2
        else:
            to_lst = lst2
            from_lst = lst1
        break
    else:
        return lst1 + lst2

    while from_lst:
        i = bisect.bisect(to_lst, from_lst[0])
        to_lst.insert(i, from_lst[0])
        from_lst[:] = from_lst[1:]
        res.extend(to_lst[:i])
        to_lst[:] = to_lst[i:]

        if not to_lst:
            res.extend(from_lst)
            return res

        i = 0
        for i, el in enumerate(from_lst):
            if el <= to_lst[0]:
                res.append(el)
                i += 1
            else:
                break
        from_lst[:] = from_lst[i:]

    res.extend(to_lst[:])

    return res


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode],  # noqa: N802
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        res = merge(to_list(list1), to_list(list2))
        return to_node(res)

    def process(self, *args, **kwargs):
        return self.mergeTwoLists(*args, **kwargs)
