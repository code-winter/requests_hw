import requests


class Yandex:
    """
    Class for working with Yandex API
    """
    def __init__(self, token):
        self.token = token

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth ' + self.token
        }

    def _get_upload_url(self, remote_file_path):
        """
        Constructs URI for upload

        :param remote_file_path: contains a path to a remote folder
        :return: dict with href
        """
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self._get_headers()
        params = {"path": remote_file_path, "overwrite": "true"}
        response = requests.get(url=url, headers=headers, params=params)
        return response.json()

    def upload_to_disk(self, remote_file_path, filename):
        """
        Uploads local file to a remote folder

        :param remote_file_path: path to a remote folder
        :param filename: file name in local folder
        :return: nothing
        """
        href = self._get_upload_url(remote_file_path)
        response = requests.put(href['href'], data=open(filename, 'rb'))
        if response.status_code == 201:
            print('Success')
        else:
            print('Uh-oh')
