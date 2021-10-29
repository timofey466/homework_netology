import os


path = os.path.join(os.getcwd(), 'cook_book.txt')

with open(path, encoding='utf-8') as file:
    result = {}
    name_food = file.readline()
    num_food = int(file.readline())
    for item in range(num_food):
        person_food = []
        name, count, number = file.readline().split('|')
        person_food.append(
            {'name': name, 'count': count, 'number': number}
        )
        result[name_food] = person_food
    print(result)
    zero = file.readline()
    cook_result_one = {}
    new_name_fod = file.readline()
    new_num_fod = int(file.readline())
    for item in range(new_num_fod):
        new_person_fod = []
        new_name, new_count, new_number, = file.readline().split('|')
        new_person_fod.append(
            {'name': new_name, 'count': new_count, 'number': new_number,}
        )
        cook_result_one[new_name] = new_person_fod
        print(cook_result_one)
    one = file.readline()
    finish = {}
    surname_food = file.readline()
    person_num = int(file.readline())
    for item in range(person_num):
        data_fod = []
        data, counter, add = file.readline().split('|')
        data_fod.append(
            {'name': data, 'count': counter, 'number': add}
        )
        finish[surname_food] = data_fod
    print(finish)
    two = file.readline()
    over = {}
    surname_fod = file.readline()
    new_person_num = int(file.readline())
    for item in range(new_person_num):
        new_data_fod = []
        new_data, new_counter, new_add = file.readline().split('|')
        new_data_fod.append(
            {'name': new_data, 'count': new_counter, 'number': new_add}
        )
        over[surname_fod] = new_data_fod
    print(over)


x = 'омлет'
y = 'утка по-пекински'
z = 'запеченый картофель'
f = 'Фахитос'
what_eat = input('введите что будете есть:')
much_eat = input('введите сколько порций должно быть:')
if x in what_eat:
    count * much_eat
elif y in what_eat:
    new_count * much_eat
elif z in what_eat:
    counter * much_eat
elif f in what_eat:
    new_counter * much_eat