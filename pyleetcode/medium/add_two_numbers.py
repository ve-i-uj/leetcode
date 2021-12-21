import itertools
from typing import Optional

# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(list_node: ListNode) -> list:
    lst = []
    node = list_node
    lst.append(node.val)
    while node.next is not None:
        node = node.next
        lst.append(node.val)
    return lst


def to_list_node(lst: list[int]) -> ListNode:
    root = ListNode(lst[0])
    last = root
    for val in lst[1:]:
        node = ListNode(val)
        last.next = node
        last = node

    return root


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = to_list(l1)
        lst2 = to_list(l2)
        first = []
        second = []
        for i, j in itertools.zip_longest(lst1, lst2, fillvalue=0):
            first.append(str(i))
            second.append(str(j))
        first = ''.join(reversed(first))
        second = ''.join(reversed(first))

        total = int(first) + int(second)
        res = [int(i) for i in reversed(str(total))]

        return to_list_node(res)


if __name__ == '__main__':
    res = Solution().addTwoNumber(to_list_node([2,4,3]), to_list_node([5, 6, 4]))
    print(res)