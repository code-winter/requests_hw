import requests


class Yandex:
    def __init__(self, token):
        self.token = token

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth ' + self.token
        }

    def _get_upload_url(self, local_file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self._get_headers()
        params = {"path": local_file_path, "overwrite": "true"}
        response = requests.get(url=url, headers=headers, params=params)
        return response.json()

    def upload_to_disk(self, local_file_path, filename):
        href = self._get_upload_url(local_file_path)
        response = requests.put(href['href'], data=open(filename, 'rb'))
        if response.status_code == 201:
            print('Success')
        else:
            print('Uh-oh')
