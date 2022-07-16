import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = ...  # input TOKEN from Yandex API
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_folder(path):
    path_folder = requests.put(f'{URL}?path={path}', headers=headers)
    return path_folder.status_code


print(create_folder('Test'))
