import os


class FileChecker:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_exists(self):
        check = os.path.isfile(self.file_path)
        if not check:
            if os.path.dirname(self.file_path):
             os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
             with open(self.file_path, "w") as file:
                file.write("[]")
        return check