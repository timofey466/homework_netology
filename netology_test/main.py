import requests

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def people(documents):
    x = input("Номер документа ")
    for letters in documents:
        if letters["number"] == x:
            return letters["name"]


def shell(directories):
    x = input("Номер документа ")
    for letters in directories.items():
        if x in letters[1]:
            return letters[0]


def lost(documents):
    for letters in documents:
        return letters["type"], letters["number"], letters["name"]


def add(directories, documents):
    x = list(input("Тип, номер, имя и полку(Через запятую").split(", "))
    documents.append({"type": x[0], "number": x[1], "name": x[2]})
    if x[2] not in directories:
        while x[2] not in directories:
            print(f'такой полки не существует введите существующую полку({directories.keys()})')
            x = list(input("Тип, номер, имя и полку(Через запятую").split(", "))
    directories[x[3]].append(x[1])
    yield documents
    return directories



def search():
    re = input("введите команду(p,l,a,s)")
    if re == "p":
        return people(documents)
    if re == "s":
        return shell(directories)
    if re == "l":
        return lost(documents)
    if re == "a":
        return add(directories, documents)

def upload_file_to_disk(self, disk_file_path, filename):
    ref = self._get_upload_link(disk_file_path=disk_file_path).get("ref", "")
    responce = requests.put(ref, data=open(filename, 'rb'))
    responce.raise_for_status()


print(search())
