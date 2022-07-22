import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        for file in file_path:
            print(os.path.basename(file))
            response_get = requests.get(
                'https://cloud-api.yandex.net/v1/disk/resources/upload', 
                headers={
                    'Authorization': f'OAuth {self.token}'
                    }, 
                params={
                    'path': os.path.basename(file),
                    'overwrite': 'true'
                    }
            )
            
            json_data_from_get = response_get.json()
            download_link = json_data_from_get['href']

            with open(file) as f:
                response_put = requests.put(
                    download_link, 
                    files={'file': f}
                )

            print(response_put)            


if __name__ == '__main__':
    path_to_file = ["files_to_send/1.txt", "files_to_send/2.txt"]
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)