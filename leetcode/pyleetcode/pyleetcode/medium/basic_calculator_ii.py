"""227. Basic Calculator II

https://leetcode.com/problems/basic-calculator-ii/
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any

MAX_VALUE = 2**31 - 1
MIN_VALUE = -1 * (2 ** 31)

SUM_OPS = set(['-', '+'])
MUL_OPS = set(['*', '/'])
OPS = SUM_OPS | MUL_OPS
SPACE: str = ' '
INTS: set[str] = set(str(i) for i in range(10))


@dataclass
class IntResult:
    value: int
    next_i: int


@dataclass
class StrResult:
    value: str
    next_i: int


def get_int(s: str, start: int) -> IntResult:
    i = start
    int_starts = False
    while i < len(s):
        if int_starts and s[i] not in INTS:
            break

        if not int_starts and s[i] == SPACE:
            i += 1
            continue

        if s[i] in INTS:
            int_starts = True
            i += 1
            continue

    return IntResult(int(s[start:i]), i)


def get_op(s: str, start: int) -> StrResult:
    i = start
    while i < len(s):
        if s[i] == SPACE:
            i += 1
            continue
        break

    assert s[i] in OPS

    return StrResult(s[i], i + 1)


def calc_mult(s: str, start: int, l_val: int) -> IntResult:
    i = start
    while i < len(s):
        if s[i] == SPACE:
            i += 1
            continue
        op_res = get_op(s, i)
        if op_res.value == '*':
            r_res = get_int(s, op_res.next_i)
            l_val = l_val * r_res.value
            i = r_res.next_i
        elif op_res.value == '/':
            r_res = get_int(s, op_res.next_i)
            l_val = l_val // r_res.value
            i = r_res.next_i
        else:
            # Это или сложение или вычитание
            break

    return IntResult(l_val, i)


class Solution:

    def process(self, *args, **kwargs):
        return self.calculate(*args, **kwargs)

    def calculate(self, s: str) -> int:
        l_res = get_int(s, 0)
        i = l_res.next_i
        l_val = l_res.value
        while i < len(s):
            if s[i] == SPACE:
                i += 1
                continue
            op_res = get_op(s, i)
            if op_res.value in MUL_OPS:
                # Если мы получили умножение или деление, можно сразу
                # посчитать правое выражение до конца строки или до знака плюс
                # l_val * r_val --> l_val
                r_res = calc_mult(s, i, l_val)
                l_val = r_res.value
                i = r_res.next_i
                continue
            # Это или плюс или минус между операндами. Нужно проверить,
            # участвует ли правый операнд в умножении или делении.
            r_res = get_int(s, op_res.next_i)
            if r_res.next_i < len(s):
                # Но проверять его нужно только если строка не закончилась.
                # В обратном случае учитывать следующий операнд не нужно.
                next_op_res = get_op(s, r_res.next_i)
                if next_op_res.value in MUL_OPS:
                    # l_val + r_val * rr_val --> l_val + r_val
                    rr_res = calc_mult(s, r_res.next_i, r_res.value)
                    r_val = rr_res.value
                    i = rr_res.next_i
                else:
                    # l_val + r_val + rr_val --> (l_val + r_val) + rr_val
                    r_val = r_res.value
                    i = r_res.next_i
            else:
                r_val = r_res.value
                i = r_res.next_i

            if op_res.value == '+':
                l_val = l_val + r_val
            else:
                l_val = l_val - r_val

            if l_val > MAX_VALUE:
                l_val = MAX_VALUE
            if l_val < MIN_VALUE:
                l_val = MIN_VALUE

        return l_val
