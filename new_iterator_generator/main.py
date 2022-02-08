class FlatIterator:
    def __init__(self, lst):
        self.lst = lst
        self.cursor = -1
        self.list_len = len(self.lst)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self.lst[self.cursor]):
          iter(self)
        if self.cursor == self.list_len:
          raise StopIteration
        self.nest_cursor += 1
        return self.lst[self.cursor][self.nest_cursor - 1]

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
'''задание №1'''
#    for item in FlatIterator(nested_list):
 #       print(item)
'''задание №2'''


def generation(list):
    for letters in list:
        if type(letters) == int or letters == float or letters == str or letters == bool:
            yield letters
        else:
           for i in letters:
               if type(letters) == int or letters == float or letters == str or letters == bool:
                   yield letters




print(generation(nested_list))







