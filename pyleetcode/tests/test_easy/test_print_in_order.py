"""Unit tests of "1114. Print in Order".

https://leetcode.com/problems/print-in-order/
"""

from concurrent.futures import thread
import functools
from threading import Thread, Event

import pytest

from pyleetcode.easy.print_in_order import Foo


TEST_CASES = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


@pytest.mark.parametrize('order', TEST_CASES)
def test(capsys, order: list[int]):
    final_lock = Event()
    final_lock.clear()
    inst: Foo = Foo(final_lock)

    threads = {
        1: Thread(target=inst.first, args=(functools.partial(print, 'first'), )),
        2: Thread(target=inst.second, args=(
            functools.partial(print, 'second'), )),
        3: Thread(target=inst.third, args=(functools.partial(print, 'third'), )),
    }
    for i in order:
        t = threads[i]
        t.start()
    final_lock.wait()

    captured = capsys.readouterr()
    assert captured.out.replace('\n', '') == 'firstsecondthird'
