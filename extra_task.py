import  types

from flatiterator import flat_generator


# Task 3
class NewFlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.flat_list = self.get_flat_list(self.list_of_list)
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.cursor]

    def get_flat_list(self, inner_lists):
        result = []
        for item in inner_lists:
            if not isinstance(item, list):
                result.append(item)
            else:
                result.extend(self.get_flat_list(item))
        return result

    # Task 4
def new_flat_generator(list_of_list):
    for item in list_of_list:
        if not isinstance(item, list):
            yield item
        else:
            yield from new_flat_generator(item)

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            NewFlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(NewFlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            new_flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(new_flat_generator(list_of_lists_2)) == ['a', 'b', 'c',
                                                         'd',
                                                     'e', 'f', 'h', False,
                                                     1, 2, None, '!']

    assert isinstance(new_flat_generator(list_of_lists_2),
                      types.GeneratorType)


if __name__ == '__main__':

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    # Проверка решения задачи 3
    for item in NewFlatIterator(list_of_lists_2):
        print(item)

    test_3() # Тест решения задачи 3

    # Проверка решения задачи 4
    for item in new_flat_generator(list_of_lists_2):
        print(item)

    test_4() # Тест решения задачи 4