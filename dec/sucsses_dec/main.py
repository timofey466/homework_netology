import datetime
import os

file_name = 'info.txt'
path = os.path.join(os.getcwd(), "info.txt")
ref = os.path.join(os.getcwd(), 'main.py')


def decorate():
    def dec_one(function):
        def write_character(*args, **kwargs):
            with open(path, "w") as file:
                pacher = datetime.datetime.now()
                file.write(f'функция была вызвана в {pacher}\n')
                title = function.__name__
                file.write(f'имя функции {title}\n')
                file.write(f'функция была вызвана с аргументами {*args, kwargs}\n')
                result = function(*args, **kwargs)
                file.write(f'функция была вызвана с результатом {result}\n')
                return result
        return write_character

    return dec_one


def parametrized_decor():
    def decor(function):
        def new_foo(*args, **kwargs):
            with open(path, "w") as file:
                pacher = datetime.datetime.now()
                title = function.__name__
                result = function(*args, **kwargs)
                file.write(f'функция была вызвана в {pacher}\n')
                file.write(f'имя функции {title}\n')
                file.write(f'функция была вызвана с аргументами {*args, kwargs}\n')
                file.write(f'место вызова функции {ref}\n')
                file.write(f'место записи финкции {path}\n')
                file.write(f'функция была вызвана с результатом {result}\n')
                return result
        return new_foo
    return decor
