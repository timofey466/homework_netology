import os
from pprint import pprint

path = os.path.join(os.getcwd(), '1.txt')
path_two = os.path.join(os.getcwd(), '2.txt')
path_three = os.path.join(os.getcwd(), '3.txt')

with open(path, 'r' ,encoding='utf-8') as file:
    pprint(path)
    line = len(file.readlines())
    pprint(line)
    pprint(file.read())
    file.close()

with open(path_two, 'r' ,encoding='utf-8') as data:
    pprint(path_two)
    line = len(data.readlines())
    pprint(line)
    pprint(data.read())
    file.close()

with open(path_three, 'r' ,encoding='utf-8') as date:
    pprint(path_three)
    line = len(date.readlines())
    pprint(line)
    pprint(date.read())
    file.close()
