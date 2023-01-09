"""10. Regular Expression Matching

https://leetcode.com/problems/regular-expression-matching/
"""

from typing import ClassVar
from xxlimited import new


class _CharPattern:
    IS_GREEDY: ClassVar[bool] = False

    def __init__(self, ch: str = '') -> None:
        self._ch = ch

    def is_matched(self, ch: str) -> bool:
        return False

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(ch="{self._ch}")'

    __repr__ = __str__


class NoPattern(_CharPattern):
    IS_GREEDY = False


class AnyChar(_CharPattern):
    IS_GREEDY = True

    def __init__(self, ch: str = '') -> None:
        super().__init__(ch='.*')

    def is_matched(self, ch: str) -> bool:
        return True


class SingleChar(_CharPattern):
    IS_GREEDY = False

    def is_matched(self, ch: str) -> bool:
        return ch == self._ch


class RepeatedChar(_CharPattern):
    IS_GREEDY = True

    def is_matched(self, ch: str) -> bool:
        return ch == self._ch


class AnySingleChar(_CharPattern):
    IS_GREEDY = False

    def __init__(self, ch: str = '') -> None:
        super().__init__(ch='.')

    def is_matched(self, ch: str) -> bool:
        return True


class Pattern:
    ASTERISK = '*'
    DOT = '.'
    _SPECIAL_CHARS = [ASTERISK, DOT]

    def __init__(self, patt: str):
        self._patt = patt
        self._patterns = self._parse(patt)
        self._index = 0

    def get_last_patt_indices(self) -> list[int]:
        """Получить индексы паттернов, на остановке которых будет считаться успех.

        Если в конце стоят жадные паттерны, то при окончании строки их можно не учитывать.
        """
        res = [len(self._patterns) - 1]
        for patt_obj in reversed(self._patterns):
            if patt_obj.IS_GREEDY:
                res.append(res[-1] - 1)
                continue
            break

        return res

    def match(self, s: str) -> bool:
        last_patt_i = len(self._patterns) - 1
        last_i = len(s) - 1

        stack: list[tuple[int, int]] = [(0, 0)]
        while stack:
            # Сперва нужно отсечь все ложные результаты
            i, patt_i = stack.pop()
            if i >= len(s) or patt_i >= len(self._patterns):
                continue

            ch = s[i]
            patt_obj = self._patterns[patt_i]

            if not patt_obj.is_matched(ch):
                if patt_obj.IS_GREEDY:
                    # Паттерн жадный, его может не быть, проверим на совпадение
                    # туже букву, но следующий паттерн
                    stack.append((i, patt_i + 1))
                continue

            # Мы добрались до последнего паттерна, который ".*", а значит примет оставшиеся символы
            if patt_i == last_patt_i and isinstance(patt_obj, AnyChar):
                return True

            if i == last_i and patt_i in self.get_last_patt_indices():
                return True

            # Проверим на совпадение этому паттерну следующую букву
            if patt_obj.IS_GREEDY:
                stack.append((i + 1, patt_i))
                # Паттерн жадный, его может не быть, проверим на совпадение
                # туже букву, но следующий паттерн
                stack.append((i, patt_i + 1))
            else:
                stack.append((i + 1, patt_i + 1))

        return False

    def _parse(self, patt: str) -> list[_CharPattern]:
        i = 0
        patterns: list[_CharPattern] = []
        while i < len(patt):
            ch = patt[i]
            next_ch = patt[i + 1] if i + 1 < len(patt) else ''

            # Если это точка и следующий элемент не астериск
            if ch == self.DOT and next_ch != self.ASTERISK:
                patterns.append(AnySingleChar())
                i += 1
                continue

            if ch == self.DOT and next_ch == self.ASTERISK:
                patterns.append(AnyChar())
                i += 2
                continue

            # Элемент точно не точка и не астериск

            if next_ch == self.ASTERISK:
                patterns.append(RepeatedChar(ch))
                i += 2
                continue

            patterns.append(SingleChar(ch))
            i += 1

        new_patterns = [patterns[0]]
        for patt_obj in patterns[1:]:
            if patt_obj.IS_GREEDY and patt_obj == new_patterns[-1]:
                continue
            new_patterns.append(patt_obj)

        # За .* жадные паттерны не нужны - это тоже самое
        new_patterns = []
        any_char: bool = False
        for patt_obj in patterns:
            if isinstance(patt_obj, AnyChar) and not any_char:
                any_char = True
                new_patterns.append(patt_obj)
                continue

            if not patt_obj.IS_GREEDY:
                any_char = False

            if any_char and patt_obj.IS_GREEDY:
                continue

            new_patterns.append(patt_obj)

        return new_patterns


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        return Pattern(p).match(s)
