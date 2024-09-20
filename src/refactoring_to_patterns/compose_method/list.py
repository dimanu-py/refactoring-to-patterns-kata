from typing import Any


class CustomList:

    _elements: list[Any]
    _size: int
    _read_only: bool

    def __init__(self, read_only: bool) -> None:
        self._read_only = read_only
        self._size = 0
        self._elements = []

    def add(self, element: Any) -> None:
        if not self._read_only:
            if self._list_is_full():
                self._increase_size_by(10)

            self._add(element)

    def _add(self, element: Any) -> None:
        self._elements[self._size] = element
        self._size += 1

    def _list_is_full(self) -> bool:
        new_size = self._size + 1
        return new_size > len(self._elements)

    def _increase_size_by(self, amount: int) -> None:
        new_elements = [None] * (len(self._elements) + amount)
        for i in range(self._size):
            new_elements[i] = self._elements[i]
        self._elements = new_elements

    def elements(self) -> list[Any]:
        return self._elements
