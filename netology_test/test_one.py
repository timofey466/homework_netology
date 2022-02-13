from main import people, shell, add, lost, documents, directories

firts_brige = ['2207 876234', '11-2']

def test_people_one():
    assert people('2207 876234') == 'Василий Гупкин'
def test_people_two():
    assert  people('11-2') == 'Геннадий Покемонов'
def test_people_three():
    assert people('10006') == 'Аристарх Павлов'
def test_shell_one():
    assert shell(firts_brige) == '1'
def test_shell_two():
    assert shell('10006') == '2'
def test_lost_one():
    assert lost('passport') == '2207 876234'
def test_lost_two():
    assert  lost('2207 876234') == 'Василий Гупкин'
def test_lost_three():
    assert lost('invoice') == '11-2'
def test_lost_four():
    assert lost('11-2') == 'Геннадий Покемонов'
def test_lost_five():
    assert lost('insurance') == '10006'
def test_lost_six():
    assert  lost('10006') == 'Аристарх Павлов'
def test_add_one():
    assert add('type') == 'passport' or 'invoice' or 'insurance'
def test_add_two():
    assert add('number') == '2207 876234' or '11-2' or '10006'
def test_add_three():
    assert  add('name') == 'Аристарх Павлов' or 'Геннадий Покемонов' or 'Василий Гупкин'


