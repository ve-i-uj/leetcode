"""100. Same Tree

https://leetcode.com/problems/same-tree/
"""

from typing import Optional, List, Any  # noqa: F401


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'

    __repr__ = __str__


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isSameTree(*args, **kwargs)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            p = stack_p.pop()
            q = stack_q.pop()

            if p is None and q is None:
                continue

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            stack_p.append(p.left)
            stack_p.append(p.right)

            stack_q.append(q.left)
            stack_q.append(q.right)

        if stack_p or stack_q:
            return False

        return True
