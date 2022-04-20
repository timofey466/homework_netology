import csv
from datetime import datetime

from phones.models import Phone


def handle(self, *args, **options):
    phone_data = []
    with open('phones.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            phone_data.append(', '.join(row).split(';'))
    phone_data.pop(0)
    name = []
    number = []
    photo = []
    year = []
    have = []
    for i in phone_data:
        name.append(i[1])
        number.append(i[3])
        photo.append(i[2])
        year.append(i[4])
        have.append(i[5])
    all_orm = list(zip(name, number, photo, year, have))

    phone_one = Phone(title=str(all_orm[0][0]), price=int(all_orm[0][1]), image=all_orm[0][2],
                      date=datetime.strptime(all_orm[0][3], "%Y-%m-%d"), lte_exists=bool(all_orm[0][4]))
    phone_one.save()

    phone_two = Phone(title=str(all_orm[1][0]), price=int(all_orm[1][1]), image=all_orm[1][2],
                      date=datetime.strptime(all_orm[1][3], "%Y-%m-%d"), lte_exists=bool(all_orm[1][4]))
    phone_two.save()

    phone_three = Phone(title=str(all_orm[2][0]), price=int(all_orm[2][1]), image=all_orm[2][2],
                        date=datetime.strptime(all_orm[2][3], "%Y-%m-%d"), lte_exists=bool(all_orm[2][4]))
    phone_three.save()


print(handle())
