"""155. Min Stack

https://leetcode.com/problems/min-stack/
"""


class MinStack:

    def __init__(self):
        self._stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        if not self._stack:
            self._stack.append((val, val))
            return
        _, last_min = self._stack[-1]
        self._stack.append((val, min(val, last_min)))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]
