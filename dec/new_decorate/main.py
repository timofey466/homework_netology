from datetime import datetime
import os

path = os.path.join(os.getcwd(), 'info.txt')
ref = os.path.join(os.getcwd(), 'main.py')

def dec_one(function):
    def write_character(*args, **kwargs):
        with open(path, encoding='utf-8') as file:
            pacher = datetime.now()
            file.write(f'функция была вызвана в {pacher}')
            title = function.__name__
            file.write(f'имя функции {title}')
            file.write(f'функция была вызвана с аргументами {*args, kwargs}')
            result = function(*args, **kwargs)
            file.write(f'функция была вызвана с результатом {result}')
        file.close()
    return write_character

def parametrized_decor(parameter):
    def decor(function):
        def new_foo(*args, **kwars):
            with open(path, encoding='utf-8') as file:
                pacher = datetime.now()
                title = function.__name__
                result = function(*args, kwars)
                if parameter == 'date':
                    file.write(f'функция была вызвана в {pacher}')
                elif parameter == 'name':
                    file.write(f'имя функции {title}')
                elif parameter == 'args_kwargs':
                    file.write(f'функция была вызвана с аргументами {*args, kwars}')
                elif parameter == 'home':
                    file.write(f'место вызова функции {ref}')
                elif parameter == 'info':
                    file.write(f'место записи финкции {path}')
                elif parameter == 'result':
                    file.write(f'функция была вызвана с результатом {result}')
            file.close()
        return new_foo
    return decor

