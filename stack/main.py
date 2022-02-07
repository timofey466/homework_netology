class Stack:
    def isEmpty(self, l):
        if len(l) == 0:
            return False
        else:
            return True

    def push(self, l, o):
        list(l).insert([0], o)


    def pop(self, l):
        self.ind = l[0]
        type_l = type(l)
        if type_l == int or type_l == float or type_l == bool or type_l == str or type:
            print('эта функция работает только с типом list')
        clear = Stack.isEmpty(l)
        if clear == False:
            print("список не должен быть пустым")
        elif type_l == list:
            list(l).remove(self.ind)
        return self.ind

    def peek(self, l):
        first_peek = l[0]
        return first_peek

    def size(self, l):
        size_one = len(l)
        size_many = Stack.isEmpty(l[0])
        num = range(0, size_one)
        if size_many == False:
            pass
        elif size_many == True:
            for i in l:
                for n in num:
                    print(f'object {n} : {len(i)}')



    def find_balance(self, l):
        help_find = []
        for letters in l:
            if letters == '(':
                help_find.append('(')
                if letters == ')':
                    help_find.remove('(')

            if letters == '[':
                help_find.append('[')
                if letters == ']':
                    help_find.remove('[')

            if letters == '{':
                help_find.append('{')
                if letters == '}':
                    help_find.remove('{')
        result = Stack.isEmpty(help_find)
        if result == False:
            return 'Success'
        else:
            return 'No balance'



