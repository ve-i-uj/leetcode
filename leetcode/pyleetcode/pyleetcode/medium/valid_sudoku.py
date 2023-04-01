"""36. Valid Sudoku

https://leetcode.com/problems/valid-sudoku/
"""

import abc
from dataclasses import dataclass
from typing import ClassVar, List


@dataclass(frozen=True)
class Position:
    row: int
    column: int


class IEntity(abc.ABC):
    _TYPE: ClassVar[str]

    def __init__(self, row_i: int, column_i: int, value: str):
        self._position: Position = Position(row_i, column_i)
        self._value: str = value

    @abc.abstractmethod
    def __hash__(self) -> int:
        return super().__hash__()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._position}, value={self._value})'

    __repr__ = __str__

    @abc.abstractmethod
    def __eq__(self, __value: object) -> bool:
        return super().__eq__(__value)


class Row(IEntity):
    _TYPE = 'row'

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
            and self._position.row == other._position.row \
            and self._value == other._value

    def __hash__(self) -> int:
        return hash((self._TYPE, self._position.row, self._value))


class Column(IEntity):
    _TYPE = 'column'

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
            and self._position.column == other._position.column \
            and self._value == other._value

    def __hash__(self) -> int:
        return hash((self._TYPE, self._position.column, self._value))


class Box(IEntity):
    _TYPE = 'box'

    def __eq__(self, other):
        return isinstance(other, self.__class__) \
            and self._position == other._position \
            and self._value == other._value

    def __hash__(self) -> int:
        return hash((self._TYPE, self._position, self._value))


class Solution:

    def process(self, *args, **kwargs):  # noqa: N802
        return self.isValidSudoku(*args, **kwargs)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        entities = []
        for r_i, row in enumerate(board):
            for c_i, value in enumerate(row):
                if value == '.':
                    continue
                entities.append(Row(r_i, c_i, value))
                entities.append(Column(r_i, c_i, value))
                entities.append(Box(r_i // 3, c_i // 3, value))

        return len(entities) == len(set(entities))
