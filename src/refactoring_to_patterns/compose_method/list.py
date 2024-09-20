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
                new_elements = [None] * (len(self._elements) + 10)
                for i in range(self._size):
                    new_elements[i] = self._elements[i]
                self._elements = new_elements

            self._elements[self._size] = element
            self._size += 1

    def elements(self) -> list[Any]:
        return self._elements
