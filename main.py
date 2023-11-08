import types

'''
1. Доработать класс FlatIterator в коде ниже.
Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
т. е. последовательность, состоящую из вложенных элементов.
Функция test в коде ниже также должна отработать без ошибок.
'''
class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.iteration = 0
        self.element = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.element += 1
        if self.element >= len(self.list_of_lists[self.iteration]):
            self.iteration += 1
            self.element = 0
        if self.iteration >= len(self.list_of_lists):
            raise StopIteration
        return self.list_of_lists[self.iteration][self.element]

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


'''
2. Доработать функцию flat_generator. 
Должен получиться генератор, который принимает список списков и возвращает их плоское представление. 
Функция test в коде ниже также должна отработать без ошибок.
'''
def flat_generator(list_of_list):
    cursor = 0
    element = 0
    while cursor < len(list_of_list):
        if element < len(list_of_list[cursor]):
            yield list_of_list[cursor][element]
            element += 1
        else:
            cursor += 1
            element = 0

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


'''
3.* Необязательное задание. 
Написать итератор, аналогичный итератору из задания 1, 
но обрабатывающий списки с любым уровнем вложенности. 
'''
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.coursor = -1

    def __iter__(self):
        return self

    def recursive_func(self, some_list):
        result = []
        if not isinstance(some_list, list):
            return [some_list]
        else:
            for element in list(some_list):
                result.extend(self.recursive_func(element))

        return result

    def __next__(self):
        self.coursor += 1
        it = self.recursive_func(self.list_of_list)
        if self.coursor < len(it):
            return it[self.coursor]
            self.coursor += 1
        raise StopIteration
def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


'''
4.* Необязательное задание. 
Написать генератор, аналогичный генератору из задания 2, 
но обрабатывающий списки с любым уровнем вложенности. 
Шаблон и тест в коде ниже:
'''
def flat_generator(some_list):
    it = iter(some_list)
    while True:
        try:
            element = next(it)
            if not isinstance(element, list):
                yield element
            else:
                yield from flat_generator(element)
        except StopIteration:
            return
def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)



if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()


