import types

# Task 1
class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.outer_index = 0 # индекс внешнего списка
        self.inner_index = 0 # индекс вложенного списка
        return self

    def __next__(self):
        if self.outer_index >= len(self.list_of_list):
            raise StopIteration

        if self.inner_index >= len(self.list_of_list[self.outer_index]):
            self.outer_index += 1
            self.inner_index = 0
            return self.__next__()

        item = self.list_of_list[self.outer_index][self.inner_index]
        self.inner_index += 1
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

# Task 2
def flat_generator(list_of_lists):
    for inner_list in list_of_lists:
        for item in inner_list:
            yield item

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    # Проверка решения задачи 1
    for item in FlatIterator(list_of_lists_1):
        print(item)
    test_1()

    # Проверка решения задачи 1
    for item in flat_generator(list_of_lists_1):
        print(item)
    test_2()




