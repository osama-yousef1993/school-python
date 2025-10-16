import json


class FileHelper:
    def __init__(self):
        self.folder_path = "files/"

    def read_file(self, file_name):
        with open(f"{self.folder_path}{file_name}", "r") as file:
            return json.loads(file.read())

    def write_file(self, file_name, content):
        with open(f"{self.folder_path}{file_name}", "w") as file:
            file.write(json.dumps(content))
