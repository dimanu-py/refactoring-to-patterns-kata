from expects import expect, be_empty, equal
from src.refactoring_to_patterns.compose_method.list import CustomList


class TestCustomList:

    def test_not_add_element_when_is_read_only(self):
        custom_list = CustomList(read_only=True)

        custom_list.add(1)

        expect(custom_list.elements()).to(be_empty)

    def test_add_element(self):
        custom_list = CustomList(read_only=False)

        custom_list.add(1)

        expected_elements = [1, None, None, None, None, None, None, None, None, None]
        expect(custom_list.elements()).to(equal(expected_elements))

    def test_grow_list_if_elements_exceed_size(self):
        custom_list = CustomList(read_only=False)

        for value in range(1, 12):
            custom_list.add(value)

        expected_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None, None, None, None, None, None, None, None, None]
        expect(custom_list.elements()).to(equal(expected_elements))