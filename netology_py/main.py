import datetime
from application.salary import calculate_salary
from application.people import get_employees
from dirty_main import *

if __name__ == '__main__':
    print(datetime.date.today())
    print(calculate_salary('salary'))
    print(get_employees('people'))


