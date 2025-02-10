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


if __name__ == '__main__':
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for item in NewFlatIterator(list_of_lists_2):
        print(item)

    test_3()