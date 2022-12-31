"""108. Convert Sorted Array to Binary Search Tree

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

from __future__ import annotations

import enum
from typing import Optional, List  # noqa: F401


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: TreeNode) -> bool:
        s_stack = [self]
        o_stack = [other]
        while s_stack and o_stack:
            s_node = s_stack.pop()
            o_node = o_stack.pop()
            if s_node is None and o_node is None:
                continue

            if s_node is None and o_node is not None:
                return False
            if s_node is not None and o_node is None:
                return False
            if s_node.val != o_node.val:
                return False

            s_stack.extend([s_node.left, s_node.right])
            o_stack.extend([o_node.left, o_node.right])
        return True

    @staticmethod
    def from_list(nums: list[int]) -> TreeNode:
        return Solution.create_tree(nums)

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self)


class D(enum.Enum):
    LEFT = 0
    RIGHT = 1


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        l = 0
        r = len(nums)
        m = (l + r) // 2
        root = TreeNode(nums[m])
        res = root
        stack = [(l, m, D.LEFT, root), (m + 1, r, D.RIGHT, root)]
        while stack:
            l, r, d, root = stack.pop()
            if l >= r:
                continue
            m = (l + r) // 2
            node = TreeNode(nums[m])
            if d is D.LEFT:
                root.left = node
            else:
                root.right = node

            stack.extend([(l, m, D.LEFT, node), (m + 1, r, D.RIGHT, node)])

        return res

    def process(self, *args, **kwargs) -> Optional[TreeNode]:  # noqa: N802
        return self.sortedArrayToBST(*args, **kwargs)

    @staticmethod
    def create_tree(nums: List[int]) -> Optional[TreeNode]:

        def create(i, vals):
            if i >= len(vals) or vals[i] is None:
                return None
            node = TreeNode(vals[i])
            node.left = create(i * 2 + 1, vals)
            node.right = create(i * 2 + 2, vals)
            return node

        return create(0, nums)
