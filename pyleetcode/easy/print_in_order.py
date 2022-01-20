"""1114. Print in Order

https://leetcode.com/problems/print-in-order/
"""

import threading

from typing import Optional, List, Any  # noqa: F401


class Foo:

    def __init__(self):
        self._lock = threading.Lock()

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()


    def second(self, printSecond: 'Callable[[], None]') -> None:

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()


    def third(self, printThird: 'Callable[[], None]') -> None:

        # printThird() outputs "third". Do not change or remove this line.
        printThird()
