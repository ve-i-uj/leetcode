"""1114. Print in Order

https://leetcode.com/problems/print-in-order/
"""

from threading import Lock, Event

from typing import Callable, Optional  # noqa: F401


class Foo:

    def __init__(self, test_final_event: Optional[Event] = None) -> None:
        self._lock_1 = Lock()
        self._lock_2 = Lock()

        self._test_final_event = test_final_event or Event()

        self._lock_1.acquire()
        self._lock_2.acquire()

    def first(self, printFirst: Callable[[], None]) -> None:
        printFirst()
        self._lock_1.release()

    def second(self, printSecond: Callable[[], None]) -> None:
        with self._lock_1:
            printSecond()
        self._lock_2.release()

    def third(self, printThird: Callable[[], None]) -> None:
        with self._lock_2:
            printThird()

        self._test_final_event.set()
