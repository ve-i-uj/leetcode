"""113. Path Sum II

https://leetcode.com/problems/path-sum-ii/
"""

from __future__ import annotations

from typing import Optional, List, Any  # noqa: F401


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def create(cls, lst: list[Optional[int]]) -> Optional[TreeNode]:
        if not lst:
            return None
        val = lst[0]
        if val is None:
            return None
        root = TreeNode(val)
        nodes = [root]
        for i, v in enumerate(lst[1:]):
            if v is None:
                continue

            parent_i = i // 2
            parent = nodes[parent_i]

            is_left = i % 2
            if is_left:
                parent.left = TreeNode(v)
                nodes.append(parent.left)
            else:
                parent.right = TreeNode(v)
                nodes.append(parent.right)

        return root

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(val={self.val})'


class Solution:

    def process(self, *args, **kwargs):
        return self.pathSum(*args, **kwargs)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        res = []

        stack: list[tuple[int, TreeNode, list[TreeNode]]] = [(root.val, root, [root])]
        while stack:
            sum_, node, path = stack.pop()

            if node.left is None and node.right is None and sum_ == targetSum:
                res.append([n.val for n in path])
                continue

            if node.left is not None:
                stack.append((sum_ + node.left.val, node.left, path + [node.left]))
            if node.right is not None:
                stack.append((sum_ + node.right.val, node.right, path + [node.right]))

        return res
