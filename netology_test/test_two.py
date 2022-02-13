from main import upload_file_to_disk, upload_file_to_disk

def status(responce):
    assert upload_file_to_disk(responce.status_code) == 200
def status_one(responce):
    assert upload_file_to_disk(responce.status_code) == 201
def status_two(responce):
    assert upload_file_to_disk(responce.status_code) >= 200
def status_three(responce):
    assert upload_file_to_disk(responce.status_code) <= 200
def is_Empty_true(self, disk_file_path, filename):
    ref = self._get_upload_link(disk_file_path=disk_file_path)
    responce = requests.put(f'https://downloader.dst.yandex.ru/disk/{ref}')
    responce.raise_for_status()
    assert responce['templated'] == True
def is_Empty_false(self, disk_file_path, filename):
    ref = self._get_upload_link(disk_file_path=disk_file_path)
    responce = requests.put(f'https://downloader.dst.yandex.ru/disk/{ref}')
    responce.raise_for_status()
    assert responce['templated'] == False