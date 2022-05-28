"""Unit tests of "155. Min Stack".

https://leetcode.com/problems/min-stack/
"""

import pytest

from easy.min_stack import MinStack


def test_1():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    assert stack.getMin() == -3

    stack.pop()

    assert stack.top() == 0
    assert stack.getMin() == -2


def test_2():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-1)

    assert stack.getMin() == -2

    assert stack.top() == -1
    stack.pop()

    assert stack.getMin() == -2
