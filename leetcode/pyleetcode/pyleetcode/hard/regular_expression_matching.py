"""10. Regular Expression Matching

https://leetcode.com/problems/regular-expression-matching/
"""

from typing import ClassVar


class _CharPattern:
    IS_GREEDY: ClassVar[bool] = False

    def __init__(self, ch: str = '') -> None:
        self._ch = ch

    def is_matched(self, ch: str) -> bool:
        return False

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(ch={self._ch})'

    __repr__ = __str__


class NoPattern(_CharPattern):
    IS_GREEDY = False


class AnyChar(_CharPattern):
    IS_GREEDY = True

    def is_matched(self, ch: str) -> bool:
        return True

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(ch=*)'

    __repr__ = __str__


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
        """Получить индексы паттернов, на остановке которых будет считаться успех."""
        res = [len(self._patterns) - 1]
        for patt_obj in reversed(self._patterns):
            if patt_obj.IS_GREEDY:
                res.append(res[-1] - 1)
                continue
            break

        return res

    def match(self, s: str) -> bool:
        max_i = 0
        max_patt_i = 0
        stack: list[tuple[int, int]] = [(max_i, max_patt_i)]
        while stack:
            # Сперва нужно отсечь все ложные результаты
            i, patt_i = stack.pop()
            if i >= len(s) or patt_i >= len(self._patterns):
                continue

            ch = s[i]
            patt_obj = self._patterns[patt_i]

            # После жадного паттерна символ не совпадает.
            if not patt_obj.IS_GREEDY and not patt_obj.is_matched(ch):
                continue

            # Здесь и далее мы имеем совпадение и продолжаем проверять дальше.
            # Запоминаем максимальный индекс, на который удалось продвинуться.
            max_i = max(i, max_i)
            max_patt_i = max(patt_i, max_patt_i)

            if not patt_obj.IS_GREEDY and patt_obj.is_matched(ch):
                stack.append((i + 1, patt_i + 1))
                continue

            stack.append((i, patt_i + 1))

            if not patt_obj.is_matched(ch):
                continue

            stack.append((i + 1, patt_i))

        if max_i == len(s) - 1 and max_patt_i in self.get_last_patt_indices():
            return True
        return False

    def _parse(self, patt: str) -> list[_CharPattern]:
        i = 0
        patterns = []
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

        return patterns


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        return Pattern(p).match(s)
