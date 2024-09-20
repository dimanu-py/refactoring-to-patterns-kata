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
            new_size = self._size + 1

            if new_size > len(self._elements):
                self._increase_size_by(10)

            self._elements[self._size] = element
            self._size += 1

    def _increase_size_by(self, amount: int) -> None:
        new_elements = [None] * (len(self._elements) + amount)
        for i in range(self._size):
            new_elements[i] = self._elements[i]
        self._elements = new_elements

    def elements(self) -> list[Any]:
        return self._elements
